import contextlib

import requests
from requests.exceptions import ConnectionError


def test_requests():
    with contextlib.suppress(ConnectionError):
        requests.get("http://127.0.0.1:12345")
