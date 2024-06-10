from modules import utils


from fastapi import APIRouter
router = APIRouter()


@router.get('/')
async def kuraiorg_root():
    return utils.response({"message":"Take a look around and ask about! We're here for you."})