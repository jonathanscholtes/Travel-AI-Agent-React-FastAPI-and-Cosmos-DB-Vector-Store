import json
from pathlib import Path
from typing import List, Optional, Union
import uuid
from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader


class JSONDataLoader(BaseLoader):
    def __init__(
        self,
        content_key: Optional[str] = None,
        ):
        self._content_key = content_key


    def load_ship(self,data:list) -> List[Document]:
        """Load and return documents from the JSON file."""

        docs:List[Document]=[]
   
        #iterate through resource pages and create a Document for each page
        for element in data:
            name = element['name']
            text = element['description'] + ' '.join(element['amenities'])
            description = element['description']
            amenities = element['amenities']

            metadata = dict(
                name = name,
                description = description,
                amenities = amenities
                )

            docs.append(Document(page_content=text, metadata=metadata))
    
        return docs
        
    def load_destination(self,data:list) -> List[Document]:
        """Load and return documents from the JSON file."""

        docs:List[Document]=[]
   
        #iterate through resource pages and create a Document for each page
        for element in data:
            name = element['name']
            text = element['description'] + ' '.join(element['activities'])
            location = element['location']
            description = element['description']
            activities = element['activities']

            metadata = dict(
                name = name,
                location = location,
                description = description,
                activities = activities
                )

            docs.append(Document(page_content=text, metadata=metadata))
    
        return docs