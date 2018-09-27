"""
    create by misslove
"""
import requests
__author__ = 'misslove'

class HTTP:

    @classmethod
    def get(cls,url,return_json=True):

        result = requests.get(url)
        if result.status_code== 200:
           return  result.json() if return_json else result.text
        return {} if return_json else ''
