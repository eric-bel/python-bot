from gettext import install
from turtle import update
from urllib import request, response


import requests

TOKEN = "5543048491:AAHSUoeDz5FLvmLetSCBPwC-_fNTEWrHwh0"

URL = "https://api.telegram.org/bot{TOKEN}/{method}"

updates = "getUpdates"

url = URL.format(TOKEN=TOKEN, method=updates)

response = requests.get(url)
print(response.json())