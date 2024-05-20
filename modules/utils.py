from pathlib import Path
import json
import os
import datetime

def get_project_root() -> Path:
    return Path(__file__).parent.parent

def get_response_template():
    json_path = os.path.join(get_project_root(),'data','template_response.json')
    with open(json_path,'r') as f:
        response_template = json.load(f)
    return response_template

def get_current_date(format="%Y-%m-%d"):
    now = datetime.datetime.now(datetime.timezone.utc)
    return now.strftime(format)

def get_current_time(format='%H:%M:%S.%f'):
    now = datetime.datetime.now(datetime.timezone.utc)
    return now.strftime(format)

def build_response(response):
    format_time = response['response_time']
    response['response_time']=get_current_time(format_time)
    format_date = response['response_date']
    response['response_date'] = get_current_date(format_date)
    return response


def response(return_value={"message":"Now this is strange, you should not be seeing this."}):
    response_template = get_response_template()
    response_built = build_response(response_template)
    response_built["return"] =  return_value
    return response_built