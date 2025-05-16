import requests 
from urllib.parse import urljoin
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

from ddojodeptrackfilter.settings import settings

class DefectDojoClient:

    def __init__(
            self,
            base_url: str,
            username: str,
            password: str,
            verify_ssl: bool,
            timeout: int
            ):
        
        self.verify_ssl = verify_ssl
        self.timeout = timeout

        self.base_url = self._check_url_connection(self._sanitize_url(base_url))
        self.api_token = self._get_api_token(username,password) 
        
        self.session = requests.Session()
        self.session.headers.update({
            'content-type': 'application/json',
            'Authorization': f'Token {self.api_token}'})

    
    def _sanitize_url(self, url : str) -> str:
        url_parsed = urlparse(url)
        if url_parsed.scheme not in ("http","https") or not url_parsed.netloc:
            raise ValueError(f"Invalid URL: {url}")
        return url_parsed.geturl().rstrip("/") + "/"

    def _check_url_connection(self, url: str) -> str:
        try:
            resp = requests.head(url, 
                    timeout=self.timeout, 
                    verify = self.verify_ssl,
                    allow_redirects = False)
        except requests.RequestException as exc:
            raise RuntimeError(f"Url not reachable: {url} ({exc})")
        
        status = resp.status_code
        if 200 <= status < 300:
            return url
        if 300 <= status < 400:
            return self._get_redirected_url(url, resp)
        raise RuntimeError(f"URL '{url}' check failed with status {status}")


    def _get_redirected_url(self, original_url : str, resp: requests.Response) -> str:
        location = resp.headers.get('Location')
        if not location:
            raise RuntimeError(f"URL {original_url} redirected (status {resp.status_code}) but no Location header provided")
        return self._sanitize_url(location)

    def _get_api_token(self, username : str, password : str) -> str:
        auth_url = urljoin(self.base_url, 'api/v2/api-token-auth/')
        try:
            resp = requests.post(
                    auth_url,
                    json={'username': username, 'password': password},
                    timeout=self.timeout,
                    verify=self.verify_ssl)
            resp.raise_for_status()
        except requests.RequestException as exc:
            raise RuntimeError(f"Failed to retrieve API token: {exc}")
        
        data = resp.json()
        token = data.get('token')
        if not token:
            raise RuntimeError(f"No token in responce: {data}")
        return token

    def _request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = urljoin(self.base_url, path.lstrip('/'))
        try:
            resp = self.session.request(
                    method=method,
                    url=url,
                    timeout=self.timeout,
                    verify=self.verify_ssl,
                    **kwargs)
            
            resp.raise_for_status()
        except requests.RequestException as exc:
            raise RuntimeError(f"API request failed [{method} {url}]: {exc}")
        return resp


    def _get_paginated_parallel(
            self,
            endpoint: str,
            base_params: dict,
            limit: int,
            workers: int
        ) -> dict:

        params = base_params.copy()
        params['limit'] = limit

        first_page = self._request("GET",endpoint,params=params).json()
        total = first_page.get('count',0)
        results = first_page.get('results',[])
        offsets = list(range(limit,total + limit - 1,limit))

        def get_page(offset:int):
            page_params = params.copy()
            page_params['offset'] = offset
            return self._request("GET",endpoint,params=page_params).json()

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(get_page,offset) for offset in offsets]
            for future in as_completed(futures):
                page = future.result()
                results.extend(page.get('results',[]))
                
        return self._create_merged_pages_response(first_page,total,results)
    
    def _create_merged_pages_response(
            self,
            first_page : dict,
            total : int,
            results : list,
        ) -> dict:

        resp = first_page.copy()
        resp['count'] = total
        resp['next'] = None
        resp['previous'] = None
        resp['results'] = results

        return resp

    def get_users(self) -> dict:
        resp = self._request("GET",'api/v2/users/')
        return resp.json()

    def get_findings(self,test_id: int, **params) -> dict:
        params['test'] = test_id
        return self._get_paginated_parallel(
                endpoint='api/v2/findings/',
                base_params=params,
                limit=settings.limit,
                workers=settings.workers
            )

    def get_tests(self,engagement_id: int, **params) -> dict:
        params['engagement'] = engagement_id
        return self._get_paginated_parallel(
                endpoint='api/v2/tests/',
                base_params=params,
                limit=settings.limit,
                workers=settings.workers
            )

    #TODO make method more wide, not just for findings

    def get_finding_url(self,finding_id : int):
        return f"{self.base_url}finding/{finding_id}" 

        
