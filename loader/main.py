from cosmosdbloader import CosmosDBLoader
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


#cosmosdb_loader.load_data(ship_json['ships'],'ships')
#cosmosdb_loader.load_data(destinations_json['destinations'],'destinations')

cosmosdb_loader.load_vectors(ship_json['ships'],'ships')
cosmosdb_loader.load_vectors(destinations_json['destinations'],'destinations')

#data ={'data':[]}
#for ship in ship_json['ships']:
#        data['data'].append({'name':ship['name'],'type':'ship','text':(ship['description'] + ' '.join(ship['amenities']))})

#for dest in destinations_json['destinations']:
#        data['data'].append({'name':dest['name'],'type':'destination','text':(dest['description'] + ' '.join(dest['activities']))})

#cosmosdb_loader.load_vectors(data['data'],'resources')
