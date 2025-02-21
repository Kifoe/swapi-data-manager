import pandas as pd
import logging
from SWAPIClient import SWAPIClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ExcelSWAPIClient(SWAPIClient):
    def __init__(self, path: str):
        self.path = path
        self.data = pd.read_excel(path, sheet_name=None)

    def fetch_json(self, endpoint: str) -> list:
        if endpoint not in self.data:
            logger.warning(f"Endpoint {endpoint} не знайдено в {self.path}")
            return []

        return self.data[endpoint].to_dict(orient='records')
