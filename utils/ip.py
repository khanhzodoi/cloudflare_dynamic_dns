import requests
from requests.exceptions import RequestException  

def get_public_ip():
    try:
        with requests.get('https://httpbin.org/ip') as response:
            if response.status_code == 200:
                data = response.json()
                return data['origin']
    except RequestException as e:  # Catch network-related exceptions
        print('An error occurred during the request:', str(e))

    return None
