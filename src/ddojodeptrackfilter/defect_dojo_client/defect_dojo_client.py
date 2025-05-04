import requests 
from urllib.parse import urljoin
from urllib.parse import urlparse

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


    def get_users(self) -> dict:
        resp = self._request("GET",'api/v2/users/')
        return resp.json()






