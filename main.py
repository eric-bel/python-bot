from gettext import install
from lib2to3.pgen2 import token
from turtle import update
import json
import const
import time
import requests
from urllib import request, response
import const
from pprint import pprint

def main():
    while True:
        url = const.URL.format(TOKEN=const.TOKEN, method=const.UPDATE_METH)
        content = requests.get(url).text
        data = json.loads(content)
        pprint(data)
        time.sleep(2)


if __name__ == "__main__":
    main()
