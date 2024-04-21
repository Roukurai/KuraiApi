from fastapi import APIRouter
from models.minecraft_item import Item

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
    return {"message":"Hey! Don't go snooping around my stuff okay?","endpoints":endpoints}


@router.get('/inventory')
async def get_inventory():
    return {"space1":"content","space2":"content","space3":"content","space4":"content","space5":"content"}

@router.post('/inventory/add_item')
async def inventory_add_item(item:Item):
    
    return {"message":"Item added Successfully","item_name":item.name,"item_id":item.id,"item_data":item}