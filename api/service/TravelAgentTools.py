from langchain_core.tools import tool
from langchain.docstore.document import Document

from data.mongodb import travel
from model.travel import Ship


@tool
def vacation_lookup(input:str) -> list[Document]:
    """find information on vacations and trips"""
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


@tool
def book_cruise(itinerary_name:str, passenger_name:str, room_name: str )-> str:
    """book cruise using itinerary name and passenger name and room name"""
    print(f"Iteinerary: {itinerary_name} passenger: {passenger_name} room: {room_name}")
    if passenger_name == "John Doe":
        return "May I please have your name?"
    else:        
        return "Cruise has been booked, ref number is 343242"