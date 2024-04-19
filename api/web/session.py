from fastapi import APIRouter
from service import TravelAgent
import uuid

router = APIRouter(prefix = "/session")


@router.get("/")
def get_session():
    return {'session_id':str(uuid.uuid4().hex)}