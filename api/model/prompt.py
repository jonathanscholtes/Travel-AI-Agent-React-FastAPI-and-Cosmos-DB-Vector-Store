from pydantic import BaseModel


class PromptResponse(BaseModel):
    text:str
    ResponseSeconds: float


class PromptRequest(BaseModel):
    input:str
    session_id: str