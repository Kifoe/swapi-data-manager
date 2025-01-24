from SWAPIClient import SWAPIClient
from SWAPIDataManager import SWAPIDataManager

client = SWAPIClient(base_url="https://swapi.dev/api/")
manager = SWAPIDataManager(client)


manager.fetch_entity("people")
manager.fetch_entity("planets")
manager.apply_filter("people", ['films', 'vehicles', 'starships', 'species'])
manager.apply_filter("planets", ['residents', 'films'])
manager.save_to_excel("data.xlsx")

print(manager.df_dict["people"].columns)