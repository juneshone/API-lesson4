import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from download_photos import download_photos


def fetch_spacex_last_launch(launch_id):
    spacex_api_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    spacex_url = response.json()['links']['flickr']['original']
    for image_number, image_url in enumerate(spacex_url):
        filename = f'images_spacex/spacex_{image_number}.jpeg'
        download_photos(spacex_api_url, filename)


if __name__ == '__main__':
    Path("C:/Users/user/Desktop/API-lesson4/images_spacex/").mkdir(parents=True, exist_ok=True)
    load_dotenv()
    launch_id = os.getenv('SPACEX_LAUNCH_ID')
    fetch_spacex_last_launch(launch_id)