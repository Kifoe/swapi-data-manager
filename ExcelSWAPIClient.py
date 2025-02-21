import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ExcelSWAPIClient:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def fetch_json(self, endpoint: str) -> list:
        sheet_name_map = {
            "people": "people",
            "planets": "planets",
            "films": "films"
        }
        if endpoint not in sheet_name_map:
            raise ValueError(f"Unknown endpoint: {endpoint}")

        sheet_name = sheet_name_map[endpoint]
        df = pd.read_excel(self.file_path, sheet_name=sheet_name)
        logger.info(f"Читання даних з файлу {self.file_path}, лист {sheet_name}")
        return df.to_dict(orient='records')
