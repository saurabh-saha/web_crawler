# util/api.py

import requests


def fetch_url_content(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return response
