from fastapi import APIRouter, HTTPException
from modules.database import SessionLocal

from modules import utils

#
# Current script will only be requested to run by Al main hive
# modules are tools not hives
#

import serial
import time
import re

# arduino = serial.Serial(port='/dev/ttyACM0',baudrate=115200)
router = APIRouter()


async def al_root():
    return utils.response({"message":"It seems you're looking for a friend"})


@router.get('/modules')
async def list_modules():
    modules_list = []
    response = utils.response({"modules_list": modules_list})
    return response

@router.post('/modules/morse')
async def send_morse_message(message):
    
    response = utils.response({"message":message})
    return response



'''
def arduino_communications(message):
    
        message = re.sub(r'\n{3,}','\n\n',message)
        print(message)
        
        arduino.flush()
        arduino.write(bytes(message, 'utf-8'))
        time.sleep(0.1)
        while True:
            data = arduino.readline().decode().strip()
            if '/420' in data:
                break
            data = data.replace("::","")
            print(data,end='',flush=True)
        print("")

# @router.post('/test')
# def arduino_communications(message):
    
#         message = re.sub(r'\n{3,}','\n\n',message)
#         print(message)
        
#         arduino.flush()
#         arduino.write(bytes(message, 'utf-8'))
#         time.sleep(0.1)
#         while True:
#             data = arduino.readline().decode().strip()
#             if '/420' in data:
#                 break
#             data = data.replace("::","")
#             print(data,end='',flush=True)
#         print("")
'''
