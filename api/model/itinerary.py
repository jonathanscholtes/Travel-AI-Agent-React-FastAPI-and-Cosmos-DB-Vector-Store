from pydantic import BaseModel


class Itinerary(BaseModel):
    ShipID:str
    Name:str

