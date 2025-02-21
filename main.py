import argparse
from SWAPIClient import SWAPIClient
from ExcelSWAPIClient import ExcelSWAPIClient
from SWAPIDataManager import SWAPIDataManager
from PlanetsProcessor import PlanetsProcessor
from PeopleProcessor import PeopleProcessor
from FilmsProcessor import FilmsProcessor

parser = argparse.ArgumentParser(description="SWAPI Data Manager")
parser.add_argument('--input', required=True, help="URL або шлях до .xlsx файлу")
parser.add_argument('--endpoints', required=True, help="Список сутностей через кому (наприклад, people,planets,films)")
parser.add_argument('--output', required=True, help="Ім'я вихідного Excel-файлу")
args = parser.parse_args()

if args.input.startswith("http"):
    client = SWAPIClient(base_url=args.input)
else:
    client = ExcelSWAPIClient(path=args.input)

manager = SWAPIDataManager(client)

manager.register_processor("people", PeopleProcessor)
manager.register_processor("planets", PlanetsProcessor)
manager.register_processor("films", FilmsProcessor)

for endpoint in args.endpoints.split(','):
    manager.fetch_entity(endpoint)

manager.save_to_excel(args.output)
print(f"Дані успішно збережено у файл {args.output}")
