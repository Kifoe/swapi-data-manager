import pandas as pd
from EntityProcessor import EntityProcessor

class FilmsProcessor(EntityProcessor):
    def process(self, json_data: list) -> pd.DataFrame:
        df = pd.DataFrame(json_data)
        df['release_date'] = pd.to_datetime(df['release_date'])
        return df
