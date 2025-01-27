import logging
import pandas as pd
from typing import Type
from SWAPIClient import SWAPIClient
from EntityProcessor import EntityProcessor

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class SWAPIDataManager:
    def __init__(self, client: SWAPIClient):
        self.client = client
        self.df_dict = {}
        self.processors = {}

    def register_processor(self, endpoint: str, processor: EntityProcessor):
        self.processors[endpoint] = processor

    def fetch_entity(self, endpoint: str):
        source_data = self.client.fetch_json(endpoint)
        processor_class = self.processors.get(endpoint, EntityProcessor)
        processor = processor_class()
        self.df_dict[endpoint] = processor.process(source_data)
        logger.info(f"Отримано {len(source_data)} записів для {endpoint}. Колонки: {self.df_dict[endpoint].columns.tolist()}")

    def apply_filter(self, endpoint: str, columns_to_drop: list):
        if endpoint in self.df_dict:
            self.df_dict[endpoint] = self.df_dict[endpoint].drop(columns=columns_to_drop, errors='ignore')
            logger.info(f'Видалено {columns_to_drop} із {self.df_dict}')
        else:
            logger.info(f'Дані для {endpoint} не знайдено')

    def save_to_excel(self, file_name):
        output_file = file_name
        logger.info(f"Запис даних у Excel файл: {output_file}")
        with pd.ExcelWriter(output_file) as writer:
            for endpoint, df in self.df_dict.items():
                df.to_excel(writer, sheet_name=endpoint, index=False)
        logger.info("Дані успішно записано у Excel.")