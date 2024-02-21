import os
import requests
from urllib.parse import urlsplit


def download_photos(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    path_parts = urlsplit(url).path
    photos_extension = os.path.splitext(path_parts)[1]
    return photos_extension
