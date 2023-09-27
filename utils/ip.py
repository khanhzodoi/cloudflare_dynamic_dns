"""Module IP providing tools to manage ip address stuffs"""
import requests
from requests.exceptions import RequestException


def get_public_ip():
    """Get current public IP of the current host"""
    try:
        with requests.get('https://httpbin.org/ip', timeout=10) as response:
            if response.status_code == 200:
                data = response.json()
                return data['origin']
    except RequestException as error:  # Catch network-related exceptions
        print('An error occurred during the request:', str(error))

    return None
