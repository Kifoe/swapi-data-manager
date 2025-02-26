import requests

from logger_config import logger


class SWAPIClient:
    def __init__(self, path: str):
        """
        Ініціалізація з базовою URL-адресою для API.
        """
        self.path = path

    def fetch_json(self, endpoint: str) -> list:
        """
        Завантажує всі сторінки JSON для вказаного endpoint.

        :param endpoint: endpoint для отримання даних (наприклад, "people")
        :return: список всіх сутностей у вигляді JSON
        """
        all_data = []
        url = f"{self.path}{endpoint}/"  # Починаємо з першої сторінки

        while url:
            # Логуємо URL запиту
            logger.info(f"Fetching data from: {url}")

            # Завантажуємо дані з API
            response = requests.get(url)
            response.raise_for_status()  # Викликає помилку, якщо статус код відповіді неправильний
            data = response.json()

            # Додаємо результати до списку
            all_data.extend(data['results'])

            # Переходимо до наступної сторінки
            url = data.get('next')

        return all_data