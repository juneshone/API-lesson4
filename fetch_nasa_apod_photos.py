import argparse
import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from download_photos import get_extension
from download_photos import download_photos


def fetch_nasa_apod_photos(nasa_api_key, count):
    nasa_api_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_api_key,
        'count': count
    }
    response = requests.get(nasa_api_url, params=payload)
    response.raise_for_status()
    for image_number, image_url in enumerate(response.json()):
        nasa_apod_url = image_url['url']
        filename = f'images/apod_{image_number}{get_extension(nasa_apod_url)}'
        download_photos(nasa_apod_url, filename, nasa_api_key)


if __name__ == '__main__':
    Path("images/").mkdir(parents=True, exist_ok=True)
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    parser = argparse.ArgumentParser(
        description='Скачивает фотографии APOD с сайта NASA'
    )
    parser.add_argument("--count", default='30', help='Количество изображений')
    args = parser.parse_args()
    fetch_nasa_apod_photos(nasa_api_key, args.count)
