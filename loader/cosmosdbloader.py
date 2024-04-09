from os import environ
from pathlib import Path
from typing import List, Optional, Union
from dotenv import load_dotenv
from pymongo import MongoClient
from jsondataloader import JSONDataLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.azure_cosmos_db import AzureCosmosDBVectorSearch, CosmosDBSimilarityType


load_dotenv(override=True)


class CosmosDBLoader():
    def __init__(
    self):
         #variable from '.env' file
        self.MONGO_CONNECTION_STRING = environ.get("MONGO_CONNECTION_STRING")
        self.DB_NAME = 'travel'

    
    def load_data(self,data:list,collection_name:str,):
        client = MongoClient(self.MONGO_CONNECTION_STRING)
        db = client[self.DB_NAME]
        collection = db[collection_name]

        collection.insert_many(data)


    def load_vectors(self,data:list,collection_name:str):
        """load embeddings  into cosmosDB vector store"""
        #hardcoded variables

        INDEX_NAME = "vectorSearchIndex"

        client = MongoClient(self.MONGO_CONNECTION_STRING)
        db = client[self.DB_NAME]
        collection = db[collection_name]

        loader = JSONDataLoader( )

        docs = None
        if collection_name == 'ships':
            docs = loader.load_ship(data)
        else:
            if collection_name == 'destinations':
                docs = loader.load_destination(data)
        

        if docs != None:
            #load documents into Cosmos DB Vector Store
            vector_store = AzureCosmosDBVectorSearch.from_documents(
                docs,
                OpenAIEmbeddings(disallowed_special=()),
                collection=collection,
                index_name=INDEX_NAME)        

            if vector_store.index_exists() == False:
                #Create an index for vector search
                num_lists = 1 #for a small demo, you can start with numLists set to 1 to perform a brute-force search across all vectors.
                dimensions = 1536
                similarity_algorithm = CosmosDBSimilarityType.COS

                vector_store.create_index(num_lists, dimensions, similarity_algorithm)


