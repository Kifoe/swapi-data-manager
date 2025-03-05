import pandas as pd
from logger_config import logger
from interfaces.DataInterface import DataProviderInterface

class ExcelSWAPIClient(DataProviderInterface):
    def __init__(self, path: str):
        self.path = path
        self.data = pd.read_excel(path, sheet_name=None)

    def fetch_data(self, endpoint: str) -> list:
        if endpoint not in self.data:
            logger.warning(f"Endpoint {endpoint} not found in {self.path}")
            return []

        return self.data[endpoint].to_dict(orient='records')