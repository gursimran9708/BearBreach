import requests
import json
import time
from tabulate import tabulate
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("VT_API_KEY")

def vt_url_api(url_to_query):
    
    url = "https://www.virustotal.com/api/v3/urls"
    
    payload={"url":url_to_query}

    headers = {
    
        "accept": "application/json",
        "x-apikey": api_key,
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, headers=headers,data=payload)
    pyresult=json.loads(response.text)
    if 'data' in pyresult and 'id' in pyresult['data']:
        
           vt_scan_id=pyresult['data']['id']
           
    else:
            return None
    url = f"https://www.virustotal.com/api/v3/analyses/{vt_scan_id}"

    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }
    time.sleep(10)

    response = requests.get(url, headers=headers)

    py_data=json.loads(response.text)
    if "data" in py_data:
        if "attributes" in py_data["data"]:
            
                    if "date" in py_data["data"]["attributes"]:
                        print("\nDate : ",py_data["data"]["attributes"]["date"],"\n")
            
                    if "stats" in py_data["data"]["attributes"]:
                        stats=py_data["data"]["attributes"]["stats"]
                        table_data = []
                        for key, value in stats.items():
                            table_data.append([key, value])
                        print("Stats :\n",tabulate(table_data, headers=["Category", "Count"],tablefmt="pretty"))
                        
                    if "results" in py_data["data"]["attributes"]:
                        results=py_data["data"]["attributes"]["results"] 
                        table_data = [[key, value['method'], value['category'], value['result']] for key, value in results.items()]
                    # Define the headers
                    headers = ["Engine Name", "Method", "Category", "Result"]
                    # Print the table
                    print("\n")
                    print(tabulate(table_data, headers=headers, tablefmt="pretty"))
                    
                    if "status" in py_data["data"]["attributes"]:
                        status=py_data["data"]["attributes"]["status"]
                        print(f"\nStatus : {status}")
                

                
            
    
    



