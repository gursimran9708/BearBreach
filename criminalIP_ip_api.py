import requests
import json
from tabulate import tabulate 
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("CRIMINALIP_API_KEY")
elements_list=["status",
"ip",
"is_malicious",
"is_vpn",
"can_remote_access",
]

def criminalIP_ip_api(ip_address):
  url = f"https://api.criminalip.io/v1/feature/ip/malicious-info?ip={ip_address}"

  payload={}
  headers = {
    "x-api-key": api_key
  }

  response = requests.get(url, headers=headers, data=payload)

  pydata=json.loads(response.text)
  for i in pydata:
    if i in elements_list:
      print(i," : ",pydata[i])
    
    
  if "ip_category" in pydata:
    if "data" in pydata["ip_category"]:
      data=pydata["ip_category"]["data"]
      headers = ['Type', 'Detect Source', 'Confirmed Time']
      table = [[d['type'], d['detect_source'], d['confirmed_time']] for d in data]
      print("\nIP Category : ")
      print(tabulate(table, headers=headers,tablefmt="pretty"))
      
  if "scanning_records" in pydata:
      scanning_records=pydata["scanning_records"]
      headers = ['Count', 'Data']
      table = [[response['count'], scanning_records['data']]]
      print("\nScanning Records : ")
      print(tabulate(table, headers=headers))
  
  if "current_opened_port" in pydata:
    if "data" in pydata["current_opened""_port"]:
      data=pydata["current_opened_port"]["data"]
      table = [[
    d['socket_type'], 
    d['port'], 
    d['protocol'], 
    d['product_name'], 
    d['product_version'], 
    d['has_vulnerability'], 
    d['confirmed_time']
      ] for d in data]
      print("\nCurrent Opened Port : ")
      print(tabulate(table, headers=headers,tablefmt="pretty"))
      
  if "ids" in pydata:
    if "data" in pydata["ids"]:
      data=pydata["ids"]["data"]
      
      table = [[
          d['classification'], 
          d['url'], 
          d['message'], 
          d['source_system'], 
          d['confirmed_time']
      ] for d in data]
      print("\nIDS : ")
      print(tabulate(table, headers=headers,tablefmt="plain"))
  
  if "vulnerability" in pydata:
    vulnerability=pydata["vulnerability"]
    headers = ['Count', 'Data']
    table = [[vulnerability['count'], vulnerability['data']]]
    print("\nVULNERABILITY : ")
    print(tabulate(table, headers=headers,tablefmt="pretty"))
    
  if "remote_port" in pydata:
    remote_port=pydata["remote_port"]
    headers = ['Count', 'Data']
    table = [[remote_port['count'], remote_port['data']]]
    print("\nRemote Port : ")
    print(tabulate(table, headers=headers,tablefmt="pretty"))


#criminalIP_ip_api("51.91.185.7")