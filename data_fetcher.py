import requests
import os
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """
    Fetches animal data from API Ninjas.
    Returns a list of animals.
    """

    url = "https://api.api-ninjas.com/v1/animals"

    response = requests.get(
        url,
        headers={
            "X-Api-Key": API_KEY
        },
        params={
            "name": animal_name
        }
    )

    if response.status_code == 200:
        return response.json()

    return []