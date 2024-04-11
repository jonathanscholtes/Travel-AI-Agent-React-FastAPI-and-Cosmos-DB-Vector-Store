
from .init import client, vector_store
from langchain.docstore.document import Document
from typing import List, Optional, Union
from model.itinerary import Itinerary

def get_ship_by_name(name:str)->str:
    db = client["travel"]
    collection_name = db["ships"]
    print(f"-{name}-")
    ship = collection_name.find_one({'name': name.strip()})
    return ship['shipid']

def itnerary_search(name:str) -> list[Itinerary]:
    data = []
    db = client["travel"]
    collection_name = db["itinerary"]
    id = get_ship_by_name(name)
    print(id)
    cursor  = collection_name.find({'ship.shipid':id})
    for item in cursor:
        data.append(Itinerary(ShipID=item['ship']['shipid'],
                              Name=item['name']
                    ))
    print(data)
    return data



def similarity_search(query:str)-> list[Document]:

    docs = vector_store.similarity_search_with_score(query,3)

    # Cosine Similarity:
    #It measures the cosine of the angle between two vectors in an n-dimensional space.
    #The values of similarity metrics typically range between 0 and 1, with higher values indicating greater similarity between the vectors.
    docs_filters = [doc for doc, score  in docs if score >=.80]

    # List the scores for documents
    for doc, score  in docs:
        print(score)

    # Print number of documents passing score threshold
    print(len(docs_filters))
  
    return docs_filters
  

