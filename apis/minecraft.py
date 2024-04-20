from fastapi import APIRouter
router = APIRouter()

@router.get('/')
async def minecraft_root():
    return {"message":"Hey! Don't go snooping around my stuff okay?"}