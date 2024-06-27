from os import environ
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.azure_cosmos_db import AzureCosmosDBVectorSearch



load_dotenv(override=False)


client: MongoClient | None = None
vector_store: AzureCosmosDBVectorSearch | None=None


def mongodb_init():
    MONGO_CONNECTION_STRING = environ.get("MONGO_CONNECTION_STRING")
    DB_NAME = "travel"
    COLLECTION_NAME = "ships"
    INDEX_NAME = "vectorSearchIndex"

    global client, vector_store
    client = MongoClient(MONGO_CONNECTION_STRING)
    vector_store = AzureCosmosDBVectorSearch.from_connection_string(MONGO_CONNECTION_STRING,
                                                                    DB_NAME + "." + COLLECTION_NAME,
                                                                    OpenAIEmbeddings(disallowed_special=()),
                                                                    index_name=INDEX_NAME )                                                                  


mongodb_init()

