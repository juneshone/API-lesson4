import datetime
import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from download_photos import get_extension
from download_photos import download_photos


def fetch_nasa_epic_photos(nasa_api_key):
    nasa_api_url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {
        'api_key': nasa_api_key,
    }
    response = requests.get(nasa_api_url, params=payload)
    response.raise_for_status()
    for image_number, image_url in enumerate(response.json()):
        nasa_epic_date = image_url['date']
        formatted_nasa_epic_date = datetime.datetime.fromisoformat(nasa_epic_date)
        formatted_date = formatted_nasa_epic_date.strftime("%Y/%m/%d")
        nasa_epic_image = image_url['image']
        nasa_epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{nasa_epic_image}.png?api_key={nasa_api_key}'
        filename = f'nasa_epic/epic_{image_number}{get_extension(nasa_epic_url)}'
        download_photos(nasa_epic_url, filename)


if __name__ == '__main__':
    Path("C:/Users/user/Desktop/API-lesson4/nasa_epic/").mkdir(parents=True, exist_ok=True)
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    fetch_nasa_epic_photos(nasa_api_key)