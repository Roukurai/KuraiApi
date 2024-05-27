from fastapi import APIRouter,HTTPException
from models.ticket import Ticket,TicketDB
from modules.database import SessionLocal

from modules import utils

router = APIRouter()

import random

@router.get('/')
async def kuraiapp_root():
    return utils.response({"message":"You seem to be up and about now!"})

@router.get('/queryTickets')
async def getQueryTicket(limit: int = 20):
    db = SessionLocal()
    try:
        ticket_items = db.query(TicketDB).filter(TicketDB.priority==1).limit(limit).all()
        if ticket_items:
            ticket_item_array = {ticket_item.id: ticket_item for ticket_item in ticket_items}
            return utils.response({"qty":len(ticket_item_array),"tickets":ticket_item_array})
        else:
            raise HTTPException(status_code=404, detail="No tickets founds")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
    
@router.post('/submit_ticket')
async def postSubmitTicket(ticket:Ticket):
    db = SessionLocal()
    ticket_item = TicketDB(**ticket.dict())
    db.add(ticket_item)
    
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=str(e))
    finally:
        db.close()
    
    return utils.response({"message":"Ticket submitted correctly aye","ticket_item":ticket})