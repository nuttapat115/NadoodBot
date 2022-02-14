import requests
import json

webhook_url = 'https://326c-203-150-199-47.ngrok.io/webhook'

data = {'name' : 'nadood',
        'channel' : 'test url'}

r = requests.post(webhook_url, data=json.dumps(data),headers={'Content-Type': 'application/json'})
print(r)