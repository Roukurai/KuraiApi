from fastapi import APIRouter, HTTPException
from modules.database import SessionLocal

from modules import utils

router = APIRouter()


@router.get('/')
async def list_modules():
    modules_list = []
    response = utils.response({"modules_list": modules_list})
    return response

@router.post('/morse')
async def send_morse_message(message):
    
    response = utils.response({"message":message})
    return response

