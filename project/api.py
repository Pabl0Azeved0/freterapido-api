import requests
import re


class Caller():

    @staticmethod
    def api_caller(param):
        data = re.sub('#', '%23', param)
        url = f'https://api.twitter.com/1.1/search/tweets.json?q={data}&result_type=recent'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAO5rEgEAAAAAY6XQhD%2Fv8RYGpDAFDwLAzAJGMyk%3DOVRe9YusS1LHKFlUOwgKpXCpUEtuYk7fxuuAhbV00pNwXf17Po'
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()
