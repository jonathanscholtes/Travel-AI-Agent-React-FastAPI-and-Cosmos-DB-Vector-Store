from fastapi import APIRouter
from service import TravelAgent
from model.prompt import PromptResponse, PromptRequest

router = APIRouter(prefix = "/agent")


@router.post("/agent_chat")
def agent_chat(prompt:PromptRequest) -> PromptResponse:
    return TravelAgent.agent_chat(prompt.input,prompt.session_id)