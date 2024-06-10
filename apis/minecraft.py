from fastapi import APIRouter,HTTPException
from models.minecraft_item import Item,ItemDB
from modules.database import SessionLocal

from modules import utils

router = APIRouter()

@router.get('/')
async def minecraft_root():
    endpoints=[]
    for route in router.routes:
        endpoint_info = {
            "path": route.path,
            "method": route.methods,
            "name": route.name,
        }
        endpoints.append(endpoint_info)
    return utils.response({"message":"Hey! Don't go snooping around my stuff okay?","endpoints":endpoints})

@router.get('/inventory')
async def get_inventory():
    return utils.response({"space1":"content","space2":"content","space3":"content","space4":"content","space5":"content"})


@router.post('/inventory/add_item')
async def inventory_add_item(item:Item):
    db = SessionLocal()
    minecraft_item = ItemDB(**item.dict())
    db.add(minecraft_item)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, details=str(e))
    finally:
        db.close()
    
    return utils.response({"message":"Item added Successfully","item_name":item.name,"item_id":item.id,"item_data":item})