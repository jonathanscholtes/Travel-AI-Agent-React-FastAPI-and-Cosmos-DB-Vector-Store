from pydantic import BaseModel
from typing import List, Optional, Union



class PromptResponse(BaseModel):
    text:str
    ResponseSeconds: float