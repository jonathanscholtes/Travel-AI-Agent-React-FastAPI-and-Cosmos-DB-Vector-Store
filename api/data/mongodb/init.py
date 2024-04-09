from os import environ
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.azure_cosmos_db import AzureCosmosDBVectorSearch
from langchain_community.cache import AzureCosmosDBSemanticCache
from langchain_community.vectorstores.azure_cosmos_db import (
    CosmosDBSimilarityType,
    CosmosDBVectorSearchType,
)


load_dotenv(override=True)


collection: Collection | None = None
vector_store: AzureCosmosDBVectorSearch | None=None
semantic_cache : AzureCosmosDBSemanticCache | None=None

def mongodb_init():
    MONGO_CONNECTION_STRING = environ.get("MONGO_CONNECTION_STRING")
    DB_NAME = "travel"
    COLLECTION_NAME = "ships"
    INDEX_NAME = "vectorSearchIndex"

    global collection, vector_store, semantic_cache
    client = MongoClient(MONGO_CONNECTION_STRING)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    vector_store = AzureCosmosDBVectorSearch.from_connection_string(MONGO_CONNECTION_STRING,
                                                                    DB_NAME + "." + COLLECTION_NAME,
                                                                    OpenAIEmbeddings(disallowed_special=()),
                                                                    index_name=INDEX_NAME )                                                                  

    
    semantic_cache = AzureCosmosDBSemanticCache(
        cosmosdb_connection_string=MONGO_CONNECTION_STRING,
        cosmosdb_client=None,
        embedding=OpenAIEmbeddings(),
        database_name=DB_NAME,
        collection_name=DB_NAME+'_CACHE',
        num_lists=1, #for a small demo, you can start with numLists set to 1 to perform a brute-force search across all vectors.,
        similarity=CosmosDBSimilarityType.COS,
        kind=CosmosDBVectorSearchType.VECTOR_IVF,
        dimensions=1536,
        m=16,
        ef_construction=64,
        ef_search=40,
        score_threshold=.99)
   

mongodb_init()

