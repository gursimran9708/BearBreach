import requests
import json
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("GREYNOISE_API_KEY")


def greynoise_ip_api(ip_address):
  url = f"https://api.greynoise.io/v3/community/{ip_address}"

  headers = {
   'key': api_key
  }

  response = requests.get(url, headers=headers)
  if response.status_code==200:
    pydata=json.loads(response.text)
    for i in pydata:
      print(i," : ",pydata[i])
  else:
    print("No results fetched")


