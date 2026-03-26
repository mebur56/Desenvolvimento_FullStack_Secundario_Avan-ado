import os
import requests
from dotenv import load_dotenv
from flask import jsonify

from src.params import NobelParams, LaureateParams

load_dotenv()
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

def nobel(params: NobelParams):
    try:
        response = requests.get(
            os.getenv("BASE_URL") + "/nobelPrizes",
            params=params.to_dict(),
            headers=headers
        )
        return response.json(), response.status_code
    except Exception as e:
        print('erro ' + str(e))

def nobelByCategory(category: str, year: int):
    try:
        response = requests.get(
            "{}/nobelPrize/{}/{}".format(os.getenv("BASE_URL"), category, year),
            headers=headers
        )
        return response.json(), response.status_code
    except Exception as e:
        print('teste erro ' + str(e))        

def laureates(params: LaureateParams):
    try:
        response = requests.get(
            os.getenv("BASE_URL") + "/laureates",
            params=params.to_dict(),
            headers=headers
        )
        return response.json(), response.status_code
    except Exception as e:
        print('erro ' + str(e))

def laureatesById(id: int):

    try:
        response = requests.get(
            "{}/laureate/{}".format(os.getenv("BASE_URL") , id),
            headers=headers
        )
        data = response.json()
        
        return data[0], response.status_code
    except Exception as e:
        print('erro ' + str(e))
