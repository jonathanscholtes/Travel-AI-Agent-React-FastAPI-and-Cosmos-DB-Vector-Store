from cosmosdbloader import CosmosDBLoader
from itinerarybuilder import ItineraryBuilder
from blobloader import BlobLoader
import json
import base64


cosmosdb_loader = CosmosDBLoader()

#ship data
with open('documents/ships.json') as file:
        ship_json = json.load(file)

#destination data
with open('documents/destinations.json') as file:
        destinations_json = json.load(file)

builder = ItineraryBuilder(ship_json['ships'],destinations_json['destinations'])
itinerary = builder.build(5)

cosmosdb_loader.load_data(itinerary,'itinerary')

#cosmosdb_loader.load_vectors(ship_json['ships'],'ships')
#cosmosdb_loader.load_vectors(destinations_json['destinations'],'destinations')


