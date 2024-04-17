import os

from slack_sdk import WebClient

from slack_sdk.errors import SlackApiError


from dotenv import load_dotenv

import requests
import json


load_dotenv()

token = os.environ['SLACK_TOKEN']


client = WebClient(token=token)

client.chat_postMessage(channel="#"+'spotify', text="Hello world!")

webhook = os.environ.get('SLACK_WEBHOOK')
headers = {'Content-type':'application/json'}
data = {'text':'Hi World!'}
res = requests.post(url=webhook, headers=headers, data=json.dumps(data))



def slack_message(webhook, message):
  headers = {'Content-type':'application/json'}
  data = {'text': message}
  res = requests.post(url=webhook, headers=headers, data=json.dumps(data))


  slack_message(webhook, 'microphone test . . .')