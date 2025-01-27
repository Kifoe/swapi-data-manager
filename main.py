from SWAPIClient import SWAPIClient
from SWAPIDataManager import SWAPIDataManager
from PlanetsProcessor import PlanetsProcessor
from PeopleProcessor import PeopleProcessor
from FilmsProcessor import FilmsProcessor

client = SWAPIClient(base_url="https://swapi.dev/api/")
manager = SWAPIDataManager(client)

manager.register_processor("people", PeopleProcessor)
manager.register_processor("planets", PlanetsProcessor)
manager.register_processor("films", FilmsProcessor)


manager.fetch_entity("people")
manager.fetch_entity("planets")
manager.fetch_entity("films")

manager.save_to_excel("data.xlsx")

print(manager.df_dict["people"].columns)
