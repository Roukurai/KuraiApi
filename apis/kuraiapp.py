from fastapi import APIRouter,HTTPException
from models.event_card import EventCard,EventCardDB
from modules.database import SessionLocal

from modules import utils

router = APIRouter()

import random

@router.get('/')
async def kuraiapp_root():
    return utils.response({"message":"You seem to be up and about now!"})

@router.get('/queryEventCard')
async def getQueryTicket(limit: int = 20):
    db = SessionLocal()
    try:
        event_card_items = db.query(EventCardDB).filter(EventCardDB.priority==1).limit(limit).all()
        if event_card_items:
            event_card_array = {event_card_item.id: event_card_item for event_card_item in event_card_items}
            return utils.response({"qty":len(event_card_array),"tickets":event_card_array})
        else:
            raise HTTPException(status_code=404, detail="No event cards founds")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
    
@router.post('/submitEventCard')
async def postSubmitTicket(event_card:EventCard):
    db = SessionLocal()
    ticket_item = EventCardDB(**event_card.dict())
    db.add(ticket_item)
    
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=str(e))
    finally:
        db.close()
    
    return utils.response({"message":"EventCard submitted correctly aye","event_card":event_card})