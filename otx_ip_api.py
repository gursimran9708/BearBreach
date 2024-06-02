import requests
import json
from rich import print
from tabulate import tabulate
from dotenv import load_dotenv
load_dotenv()
import os
otx_api_key=os.getenv("CRIMINALIP_API_KEY")


elements_list=["base_indicator","pulse_info","false_positive","validation","sections"]

def otx_ip_api(ip_address):
    url=f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip_address}/general"
    
    result=requests.get(url,headers={"X-OTX-API-KEY":otx_api_key})
    pydata=json.loads(result.text)
    for i in pydata:
        if i not in elements_list:
            print(i," : ",pydata[i])
            
    if "base_indicator" in pydata:
        base_indicator=pydata["base_indicator"]
        print("\nBase Indicator : ")
        headers = ['Key', 'Value']
        rows = [[k, v] for k, v in base_indicator.items()]
        print(tabulate(rows, headers=headers,tablefmt="pretty"))
    else:
        print("Pulse Info data not found.")  
        
    if "pulse_info" in pydata:
        pulse_info=pydata["pulse_info"]
        print("\nPulse Info : ")
        def flatten_dict(d, parent_key='', sep='_'):
            items = []
            for k, v in d.items():
                new_key = parent_key + sep + k if parent_key else k
                if isinstance(v, dict):
                    items.extend(flatten_dict(v, new_key, sep=sep).items())
                elif isinstance(v, list):
                    for i, item in enumerate(v):
                        if isinstance(item, dict):
                            items.extend(flatten_dict(item, f"{new_key}_{i}", sep=sep).items())
                        else:
                            items.append((f"{new_key}_{i}", item))
                else:
                    items.append((new_key, v))
            return dict(items)

        flat_response = flatten_dict(pulse_info)

        rows = [[k, v] for k, v in flat_response.items()]

        print(tabulate(rows))
    else:
        print("Pulse Info data not found.")   
        
    if "validation" in pydata:
        validation = pydata["validation"]
        if validation:  # Check if validation list is not empty
            print("\nValidation : ")
            headers = validation[0].keys()  # Assuming the first dictionary in validation list has all the keys
            rows = [[d['source'], d['message'], d['name']] for d in validation]
            print(tabulate(rows, headers=headers, tablefmt="pretty"))
        else:
            print("No validation data available.")
    else:
        print("Validation data not found.")
    
    if "false_positive" in pydata:
        false_positive = pydata["false_positive"]
        if false_positive:  # Check if false_positive list is not empty
            print("\nFalse Positive : ")
            headers = false_positive[0].keys() if false_positive else []  # Get headers only if false_positive list is not empty
            rows = [[d['assessment'], d['assessment_date'], d['report_date']] for d in false_positive]
            print(tabulate(rows, headers=headers, tablefmt="pretty"))
        else:
            print("No false positive data available.")
    else:
        print("False positive data not found.")  
        
        
       
