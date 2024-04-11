from fastapi import APIRouter
from service import TravelAgent
from model.promptresponse import PromptResponse

router = APIRouter(prefix = "/agent")


@router.get("/{input}")
def agent_chat(input:str) -> PromptResponse:
    return TravelAgent.agent_chat(input)