import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class SWAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_json(self, endpoint: str) -> list:

        all_data = []
        url = self.base_url + endpoint

        while url:

            logger.info(f"Отримання даних з: {url}")

            # Отримання даних з API
            response = requests.get(url)
            response.raise_for_status()  # Генерувати помилку для невдалих відповідей
            data = response.json()

            # Додавання результатів до списку
            all_data.extend(data['results'])

            # Перехід до наступної сторінки
            url = data.get('next')

        return all_data
