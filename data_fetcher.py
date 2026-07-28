import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")

API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches animal data from API Ninjas.

    Returns:
        List of animals as dictionaries.
    """

    response = requests.get(
        API_URL,
        headers={
            "X-Api-Key": API_KEY
        },
        params={
            "name": animal_name
        }
    )

    if response.status_code == 200:
        return response.json()

    else:
        print("API Error:")
        print(response.status_code)
        print(response.text)

        return []