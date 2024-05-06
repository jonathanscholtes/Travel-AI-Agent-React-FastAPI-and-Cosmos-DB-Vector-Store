import json
from pathlib import Path
from typing import List, Optional, Union
import uuid
from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader


class JSONDataLoader(BaseLoader):

    def load_ship(self,data:list) -> List[Document]:
        """Load and return documents from the JSON file."""

        docs:List[Document]=[]
   
        #iterate through ship data and create a Document for each ship
        for element in data:
            name = element['name']
            text = element['description'] + ' '.join(element['amenities'])
            description = element['description']
            amenities = element['amenities']

            metadata = dict(
                shipid = element['shipid'],
                name = name,
                description = description,
                amenities = amenities
                )

            docs.append(Document(page_content=text, metadata=metadata))
    
        return docs
        
    def load_destination(self,data:list) -> List[Document]:
        """Load and return documents from the destination JSON file."""

        docs:List[Document]=[]
   
        #iterate through destination data and create a Document for each destination
        for element in data:
            
            name = element['name']
            text = element['description'] + ' '.join(element['activities'])
            location = element['location']
            description = element['description']
            activities = element['activities']

            metadata = dict(
                destinationid = element['destinationid'],
                name = name,
                location = location,
                description = description,
                activities = activities
                )

            docs.append(Document(page_content=text, metadata=metadata))
    
        return docs