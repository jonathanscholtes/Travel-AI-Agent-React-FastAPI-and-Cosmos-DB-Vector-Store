from pydantic import BaseModel
from typing import List

class Ship(BaseModel):
    name: str
    description: str
    amenities: List[str]


class Room(BaseModel):
    name:str
    price:str



class Itinerary(BaseModel):
    ShipID:str
    Name:str
    Rooms:List[str]
    Schedule: List[str]
