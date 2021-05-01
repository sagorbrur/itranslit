
import os
import requests
from wasabi import msg

try:
    import torch
    _torch_available = True  
    msg.info(f"PyTorch version {torch.__version__} available.")
except ImportError:
    _torch_available = False 

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def download_model_and_get_path(lang, model_id):
    save_path = "itranlit-models"
    os.makedirs(save_path, exist_ok=True)
    model_path = save_path+"/"+lang+".pth"
    msg.info(f"{lang} model downloading inside {save_path}..")
    try:
        download_file_from_google_drive(
            id=model_id,
            destination=model_path
        )
        msg.good(f"{lang} model download successfull. model path {model_path}")
    except Exception as e:
        print(e)
        msg.fail(f"Fail to download {lang} model. please check exception")

 
def is_torch_available():
	return _torch_available