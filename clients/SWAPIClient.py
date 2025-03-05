import requests
from logger_config import logger
from interfaces.DataInterface import DataProviderInterface

class SWAPIClient(DataProviderInterface):
    def __init__(self, path: str):
        self.path = path

    def fetch_data(self, endpoint: str) -> list:
        all_data = []
        url = f"{self.path}{endpoint}/"

        while url:
            logger.info(f"Fetching data from: {url}")
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            all_data.extend(data['results'])
            url = data.get('next')

        return all_data
