from fastapi import APIRouter
router = APIRouter()

from uuid import uuid4
import random


from modules import utils



@router.get('/')
async def al_root():
    response = utils.response({"message":"It seems you're looking for a friend"})
    return response

@router.get('/generate_password')
async def generate_password(length: int = 12):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-'
    password = ''.join(random.choice(chars) for _ in range(length))
    response = utils.response({"password":password})
    return response

@router.get('/generate_seed')
async def generate_seed(length: int = 24):
    chars = '0123456789'
    seed = ''.join(random.choice(chars) for _ in range(length))
    response = utils.response({"seed":seed})
    return response

@router.get('/generate_uuid')
async def generate_uuid():
    response = utils.response({"uuid":str(uuid4())})
    return response

@router.get('/root_directory')
async def get_root():
    response = utils.response({"directory":utils.get_project_root()})
    return response