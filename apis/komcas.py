from fastapi import APIRouter
router = APIRouter()

from modules import utils

@router.get('/')
async def wabisabi_root():
    return utils.response({"message":"Random morse code response"}) 
