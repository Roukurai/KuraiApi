from fastapi import APIRouter
router = APIRouter()

from modules import utils

@router.get('/')
async def wabisabi_root():
    response = utils.response({"message":"Random Animal picture"})
    return response 
