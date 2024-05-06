from cosmosdbloader import CosmosDBLoader
from itinerarybuilder import ItineraryBuilder
import json


cosmosdb_loader = CosmosDBLoader(DB_Name='travel')

#read in ship data
with open('documents/ships.json') as file:
        ship_json = json.load(file)

#read in destination data
with open('documents/destinations.json') as file:
        destinations_json = json.load(file)

builder = ItineraryBuilder(ship_json['ships'],destinations_json['destinations'])

# Create five itinerary pakages
itinerary = builder.build(5)

# Save itinerary packages to Cosmos DB
cosmosdb_loader.load_data(itinerary,'itinerary')

# Save destinations to Cosmos DB
cosmosdb_loader.load_data(destinations_json['destinations'],'destinations')

# Save ships to Cosmos DB, create vector store
collection = cosmosdb_loader.load_vectors(ship_json['ships'],'ships')

# Add text search index to ship name
collection.create_index([('name', 'text')])

#cosmosdb_loader.load_vectors(destinations_json['destinations'],'destinations')


