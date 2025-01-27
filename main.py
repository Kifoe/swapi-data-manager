import argparse
from SWAPIClient import SWAPIClient
from SWAPIDataManager import SWAPIDataManager
from PlanetsProcessor import PlanetsProcessor
from PeopleProcessor import PeopleProcessor
from FilmsProcessor import FilmsProcessor

parser = argparse.ArgumentParser(description="SWAPI Data Manager")
parser.add_argument('--endpoints', required=True, help="Список сутностей через кому (наприклад, people,planets,films)")
parser.add_argument('--output', required=True, help="Ім'я вихідного Excel-файлу")
args = parser.parse_args()

client = SWAPIClient(base_url="https://swapi.dev/api/")
manager = SWAPIDataManager(client)

manager.register_processor("people", PeopleProcessor)
manager.register_processor("planets", PlanetsProcessor)
manager.register_processor("films", FilmsProcessor)

for endpoint in args.endpoints.split(','):
    manager.fetch_entity(endpoint)

manager.save_to_excel(args.output)
print(f"Дані успішно збережено у файл {args.output}")

