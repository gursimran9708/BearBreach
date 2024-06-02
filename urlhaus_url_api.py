import requests
import json
from rich import print
from tabulate import tabulate
elements_list=["query_status","id","urlhaus_reference","url","url_status","host","date_added","last_online","threat","reporter","larted","takedown_time_seconds","tags"]
def urlhaus_url_api(url_to_query):
    url = "https://urlhaus-api.abuse.ch/v1/url/"
    data = {"url": url_to_query}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        pydata=json.loads(response.text)
        
        exclude_keys = ["blacklists","payloads"]
        table_data=[[key, value] for key, value in pydata.items() if key not in exclude_keys]
        print(tabulate(table_data, tablefmt="grid"))
        

        if "blacklists" in pydata:
            print("\n","Blacklists : ")
            blacklists=pydata["blacklists"]
            # Convert response to a list of lists for tabulation
            table_data = [[key, value] for key, value in blacklists.items()]

            # Print tabulated data
            print(tabulate(table_data, headers=["Service", "Status"], tablefmt="grid"))
            
        if "payloads" in pydata:
            print("\nPayloads : ")
            payloads=pydata["payloads"]
            
            for idx, data in enumerate(payloads, start=1):
                headers = data.keys()
                table_data = [[key, value] for key, value in data.items()]
                print(f"Table {idx}:")
                print(tabulate(table_data, headers=["Field", "Value"], tablefmt="grid"))
                print("\n")
    else:
        print("Error:", response.status_code)
  

