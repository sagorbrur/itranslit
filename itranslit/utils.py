
import os
import requests
from wasabi import msg

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
    save_path = "./itranlit-models"
    os.makedirs(save_path, exist_ok=True)
    model_path = save_path+"/"+lang+".pth"
    msg.info(f"{lang} model downloading inside {save_path}..")
    download_file_from_google_drive(
        id=model_id,
        destination=model_path
    )
    msg.good(f"{lang} model download successfull. model path {model_path}")
    # return model_path


# if __name__ == "__main__":
#     file_id = '1ZeyphXpZA2RjKZIIBF9cALacROtjJgiz'
#     destination = 'test/export.pkl'
#     download_file_from_google_drive(file_id, destination)