from fastapi import APIRouter
from models.ticket import Ticket,TicketDB
from modules.database import SessionLocal

from modules import utils

router = APIRouter()

import random

@router.get('/')
async def kuraiapp_root():
    response = utils.response({"message":"You seem to be up and about now!"})
    return response

@router.post('/create_ticket')
async def create_ticket(ticket:Ticket):
    db = SessionLocal()
    ticket_entry = TicketDB(**ticket.dict())
    db.add(ticket_entry)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        error_response = {"response_code":500,"response_message":e,"object":ticket}
        # raise HTTPException(status_code=500, details=str(e))
        return error_response
    finally:
        db.close()
    
    response = utils.response({"response_code":"0000","ticket_number":id})
    return response

