from fastapi import APIRouter
router = APIRouter()

from modules import utils
response = utils.get_response_template()

@router.get('/')
async def wabisabi_root():
    response["return"] = {"message":"Random Animal picture"}
    return response 
