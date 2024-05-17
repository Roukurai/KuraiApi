from modules import utils
response = utils.get_response_template()

from fastapi import APIRouter
router = APIRouter()


@router.get('/')
async def kuraiorg_root():
    response["return"] =  {"message":"Take a look around and ask about! We're here for you."}
    return response