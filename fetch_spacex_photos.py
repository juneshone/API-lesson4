import argparse
import requests
from pathlib import Path
from download_photos import download_photos


def fetch_spacex_last_launch(launch_id):
    spacex_api_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    spacex_url = response.json()['links']['flickr']['original']
    for image_number, image_url in enumerate(spacex_url):
        filename = f'images/spacex_{image_number}.jpeg'
        download_photos(spacex_api_url, filename, api_key=None)


if __name__ == '__main__':
    Path("images/").mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Скачивает фотографии с сайта SpaceX'
    )
    parser.add_argument("--launch_id", default='latest', help='идентификатор запуска')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)
