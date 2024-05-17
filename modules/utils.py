from pathlib import Path
import json
import os

def get_project_root() -> Path:
    return Path(__file__).parent.parent

def get_response_template():
    json_path = os.path.join(get_project_root(),'data','template_response.json')
    with open(json_path,'r') as f:
        response_template = json.load(f)
    return response_template