from fastapi import APIRouter, Request, Response
from pydantic import BaseModel

from pyfullai.services.jinja import response_templates


router = APIRouter()


class HelloWorldRead(BaseModel):
    message: str

@router.get("/hello", response_model=HelloWorldRead)
async def hello() -> HelloWorldRead:
    """Return a friendly greeting."""
    return HelloWorldRead(message="Hello World!")
