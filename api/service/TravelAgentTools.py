from langchain_core.tools import tool
from langchain.docstore.document import Document
from data.mongodb import search



@tool
def travel_agent(input:str) -> list[Document]:
    """help find trips and vacations and cruise ships"""
    docs= search.similarity_search(input)
    content = "\n\n".join(doc.page_content for doc in docs)
    print("docs")
    print(len(docs))
 
    return content