import argparse
import json
import os

from clients.ExcelSWAPIClient import ExcelSWAPIClient
from processors.PeopleProcessor import PeopleProcessor
from clients.SWAPIClient import SWAPIClient
from SWAPIDataManager import SWAPIDataManager


def main():
    # Ініціалізація парсера аргументів
    parser = argparse.ArgumentParser(description="SWAPI Data Manager")
    parser.add_argument(
        "--input",
        required=True,
        help="Base API URL or path to the Excel file"
    )
    parser.add_argument(
        "--endpoint",
        type=str,
        help="Comma-separated list of entities to fetch (e.g. 'people,planets')", required=True
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output Excel file name",
        required=True
    )
    parser.add_argument(
        "--filters",
        type=str,
        help="Filters as JSON string (e.g. '{\"people\": [\"films\", \"species\"]}')",
        required=False,
        default='{}'
    )

    args = parser.parse_args()

    # Створюємо клієнт для SWAPI
    client = get_client(args.input)

    # Створюємо менеджер даних
    manager = SWAPIDataManager(client)

    # Завантажуємо та фільтруємо сутності
    endpoints = args.endpoint.split(',')
    filters = json.loads(args.filters)

    manager.register_processor("people", PeopleProcessor())

    for endpoint in endpoints:
        manager.fetch_entity(endpoint)
        if endpoint in filters:
            manager.apply_filter(endpoint, filters[endpoint])

    # Зберігаємо дані в Excel
    manager.save_to_excel(args.output)


def get_client(input_source: str):
    if input_source.startswith("http"):
        return SWAPIClient(input_source)
    elif os.path.isfile(input_source) and input_source.endswith(".xlsx"):
        return ExcelSWAPIClient(input_source)
    else:
        raise ValueError("Invalid input source. Provide a valid URL or an .xlsx file path.")


if __name__ == "__main__":
    main()