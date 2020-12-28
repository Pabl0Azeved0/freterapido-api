import requests
import json


def receitaws_api(param):
    """
    This calls receitaws api to get information from a given CNPJ.
    :param param:
    :return:
    """
    data = ''.join(filter(str.isdigit, param))
    url = f'https://www.receitaws.com.br/v1/cnpj/{data}'
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.request("GET", url, headers=headers)
    return response

def freterapido_api(param):
    """
    This calls freterapido api to get information about the JSON sended.
    :param param:
    :return:
    """
    url = 'https://freterapido.com/api/external/embarcador/v1/quote-simulator'

    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, json=json.loads(param), headers=headers)
    return response

