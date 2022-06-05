from gettext import install
from turtle import update
from urllib import request, response
import json
import requests
import const




url = URL.format(TOKEN=TOKEN, method=updates)
 
response = requests.get(url)
json_content = json.loads(response.text)
print(json_content)

# data = {
#     "chat_id": "1448024821",
#     "text": "Hello World!"
# } eric

# data = {
#     "chat_id": "1978620067",
#     "text": "Привет, любимая!"
# }

url = URL.format(TOKEN=TOKEN, method=send)
response = requests.post(url, data=data)
print(response.text)
