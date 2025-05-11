import argparse
from urllib.parse import urlparse

def validate_url(url: str) -> str:
    url_parsed = urlparse(url)
    if url_parsed.scheme not in ("http","https") or not url_parsed.netloc:
        raise argparse.ArgumentTypeError(f"Invalid URL: {url}.")
    return url_parsed.geturl().rstrip("/") + "/"

def nonempty_str(v : str) -> str:
    v_stripped = v.strip()
    if not v_stripped:
        raise argparse.ArgumentTypeError(f"Argument must not be empty or whitespace only.")
    return v_stripped

def positive_nonzero_int(v: str) -> int:
    try:
        v_int = int(v)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{v!r} is non a valid integer.")
    if v_int <= 0:
        raise argparse.ArgumentTypeError(f"{v!r} must be >= 0.")
    return v_int  
       

def parse_DDojo_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument('-b',
                        '--base-url',
                        type=validate_url,
                        required=True,
                        help="Base url of DefectDojo. Api requests will be based on it. \
                                For example: https://defectdojo/")
                       
    parser.add_argument('-u',
                        '--username',
                        type=nonempty_str,
                        required=True,
                        help="DefectDojo username.")

    parser.add_argument('-p',
                        '--password',
                        type=nonempty_str,
                        required=True,
                        help="DefectDojo password.")

    parser.add_argument('-e',
                        '--engagement-id',
                        type=positive_nonzero_int,
                        required=True,
                        help="DefectDojo engagement id.")

    parser.add_argument('-t',
                        '--timeout',
                        type=positive_nonzero_int,
                        default=60,
                        help="HTTP request timeout in seconds.")

    parser.add_argument('--no-verify-ssl',
                        action="store_false",
                        dest="verify_ssl",
                        help="Disable SSL certificate verification.")

    return parser.parse_args()



