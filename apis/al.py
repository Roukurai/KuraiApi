from fastapi import APIRouter
router = APIRouter()

from uuid import uuid4
import random


from modules import utils
response = utils.get_response_template()


@router.get('/')
async def al_root():
    return {"message":"It seems you're looking for a friend"}

@router.get('/generate_password')
async def generate_password(length: int = 12):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-'
    password = ''.join(random.choice(chars) for _ in range(length))
    response["return"] = {"password":password}
    return response

@router.get('/generate_seed')
async def generate_seed(length: int = 24):
    chars = '0123456789'
    seed = ''.join(random.choice(chars) for _ in range(length))
    response["return"] = {"seed":seed}
    return response

@router.get('/generate_uuid')
async def generate_uuid():
    response["return"] = {"uuid":str(uuid4())}
    return response

@router.get('/root_directory')
async def get_root():
    response["return"] = {"directory":utils.get_project_root()}
    return response