from langchain_core.tools import tool
from langchain.docstore.document import Document
from data.mongodb import travel
from model.travel import Ship


@tool
def vacation_lookup(input:str) -> list[Document]:
    """find information on vacations and trips"""
    ships: list[Ship] = travel.similarity_search(input)
    content = ""

    for ship in ships:
        content += f" Cruise ship {ship.name}  description: {ship.description} with amenities {'/n-'.join(ship.amenities)} "

    return content

@tool
def itinerary_lookup(ship_name:str) -> str:
    """find ship itinerary, cruise packages and destinations by ship name"""
    it = travel.itnerary_search(ship_name)
    results = ""

    for i in it:
        results += f" Cruise Package {i.Name} room prices: {'/n-'.join(i.Rooms)} schedule: {'/n-'.join(i.Schedule)}"

    return results


@tool
def book_cruise(package_name:str, passenger_name:str, room: str )-> str:
    """book cruise using package name and passenger name and room """
    print(f"Package: {package_name} passenger: {passenger_name} room: {room}")

    # LLM defaults empty name to John Doe 
    if passenger_name == "John Doe":
        return "In order to book a cruise I will need to know your name."
    else:
        if room == '':
            return "which room would you like to book"            
        return "Cruise has been booked, ref number is 343242"