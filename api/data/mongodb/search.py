
from .init import collection, vector_store
from langchain.docstore.document import Document
from typing import List, Optional, Union







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
  

