from langchain_core.tools import tool
from langchain.docstore.document import Document
from data.mongodb import travel



@tool
def travel_agent(input:str) -> list[Document]:
    """help find trips and vacations and cruise ships"""
    docs= travel.similarity_search(input)
    content = "\n\n".join(doc.page_content for doc in docs)
    print("docs")
    print(len(docs))
 
    return content

@tool
def itinerary_lookup(ship_name:str) -> str:
    """find ship itinerary by ship name"""
    it = travel.itnerary_search(ship_name)
    results = ""

    for i in it:
        results += f" Cruise Itinerary: {i.Name} "

    return results