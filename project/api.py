import requests
import re

from project.settings import token_bearer


def api_caller(param):
    """
    Twitter api calling method, with simple request in URL passing a
    parameter, you can use project/settings.py file to use your token Bearer.
    :param param:
    :return:
    """
    data = re.sub('#', '%23', param)
    url = f'https://api.twitter.com/1.1/search/tweets.json?' \
          f'q={data}&result_type=recent'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token_bearer
    }
    response = requests.request("GET", url, headers=headers)
    return response

