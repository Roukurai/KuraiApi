from fastapi import APIRouter
router = APIRouter()

@router.get('/')
async def al_root():
    return {"message":"It seems you're looking for a friend"}