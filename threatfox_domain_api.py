import requests
import json
from tabulate import tabulate
from rich import print 


def threatfox_domain_api(domain):
    url = "https://threatfox-api.abuse.ch/api/v1/"
    data = {
        "query": "search_ioc",
        "search_term": domain
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        pydata=json.loads(response.text)
        if "data" in pydata:
            results=pydata["data"]
            if type(results)==str:
                print(results)
                
            elif type(results)==list:
                for dictionary in results:
                    for key, value in dictionary.items():
                        print(f"{key}: {value}")
                    print("------------------------------------------------------------")
                
        
    else:
        print("Error:", response.status_code)
        
