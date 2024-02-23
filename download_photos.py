import os
import requests
from urllib.parse import urlsplit


def download_photos(url, filename, api_key):
    payload = {'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    path_parts = urlsplit(url).path
    photos_extension = os.path.splitext(path_parts)[1]
    return photos_extension
