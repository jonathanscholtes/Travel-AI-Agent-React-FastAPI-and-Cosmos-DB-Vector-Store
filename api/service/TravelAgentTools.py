from langchain_core.tools import tool
from langchain.docstore.document import Document

from data.mongodb import travel
from model.travel import Ship


@tool
def travel_agent(input:str) -> list[Document]:
    """help find trips and vacations and cruise ships"""
    ships: list[Ship] = travel.similarity_search(input)
    #content = "\n\n".join(doc.page_content for doc in docs)
    content = ""

    for ship in ships:
        content += f" Cruise ship {ship.name}  description: {ship.description} with amenities {'/n-'.join(ship.amenities)} "

    return content

@tool
def itinerary_lookup(ship_name:str) -> str:
    """find ship itinerary by ship name"""
    it = travel.itnerary_search(ship_name)
    results = ""

    for i in it:
        results += f" Cruise itinerary {i.Name} room prices: {'/n-'.join(i.Rooms)} schedule: {'/n-'.join(i.Schedule)}"

    return results