import requests
import json
from rich import print
from tabulate import tabulate
from dotenv import load_dotenv
load_dotenv()
import os
otx_api_key=os.getenv("OTX_API_KEY")

def otx_domain_api(domain):
    url=f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/malware"
    result=requests.get(url,headers={"X-OTX-API-KEY":otx_api_key})
    pydata=json.loads(result.text)
    if "data" in pydata:
        result=pydata["data"]
        #print(type(result))
        headers = ['datetime_int', 'hash', 'avast', 'avg', 'clamav', 'msdefender', 'date']

        # Prepare data for tabulate
        table_data = []
        for d in result:
            row = [
                d.get('datetime_int', ''),
                d.get('hash', ''),
                d['detections'].get('avast', ''),
                d['detections'].get('avg', ''),
                d['detections'].get('clamav', ''),
                d['detections'].get('msdefender', ''),
                d.get('date', '')
            ]
            table_data.append(row)

       
        print(tabulate(table_data, headers=headers, tablefmt="pretty"))
 

