import argparse
import datetime
import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from download_photos import get_extension
from download_photos import download_photos


def fetch_nasa_epic_photos(nasa_api_key, count):
    nasa_api_url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {
        'api_key': nasa_api_key,
        'count': count
    }
    response = requests.get(nasa_api_url, params=payload)
    response.raise_for_status()
    for image_number, image_url in enumerate(response.json()):
        epic_date = image_url['date']
        formatted_epic_date = datetime.datetime.fromisoformat(epic_date)
        formatted_date = formatted_epic_date.strftime("%Y/%m/%d")
        epic_image = image_url['image']
        nasa_epic_url = \
            f'https://api.nasa.gov/EPIC/archive/natural/' \
            f'{formatted_date}/png/{epic_image}.png'
        filename = f'images/epic_{image_number}{get_extension(nasa_epic_url)}'
        download_photos(nasa_epic_url, filename, nasa_api_key)


if __name__ == '__main__':
    Path("images/").mkdir(parents=True, exist_ok=True)
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    parser = argparse.ArgumentParser(
        description='Скачивает фотографии EPIC с сайта NASA'
    )
    parser.add_argument("--count", default='10', help='Количество фотографий')
    args = parser.parse_args()
    fetch_nasa_epic_photos(nasa_api_key, args.count)
