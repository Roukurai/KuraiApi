from fastapi import APIRouter
router = APIRouter()

@router.get('/')
async def wabisabi_root():
    return {"message":"Random Animal picture"}