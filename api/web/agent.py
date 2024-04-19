from fastapi import APIRouter
from service import TravelAgent
from model.promptresponse import PromptResponse

router = APIRouter(prefix = "/agent")


@router.get("/{input}/{session_id}")
def agent_chat(input:str,session_id:str) -> PromptResponse:
    
    return TravelAgent.agent_chat(input,session_id)