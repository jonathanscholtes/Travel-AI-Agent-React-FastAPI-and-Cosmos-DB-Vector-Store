from fastapi import APIRouter
from service import TravelAgent


router = APIRouter(prefix = "/agent")


@router.get("/{input}")
def agent_chat(input:str) -> str:
    return TravelAgent.agent_chat(input)