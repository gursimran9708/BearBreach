import requests
import json
from tabulate import tabulate
from rich import print
elements_list=["total","took","has_more"]
def dict_to_table(d):
    table = []
    for key, value in d.items():
        if isinstance(value, dict):
            table.append([f"{key}:", "", ""])
            nested_table = dict_to_table(value)
            table.extend(nested_table)
        else:
            table.append([key, "", value])
    return table

def print_dict_table(data):
    for idx, d in enumerate(data):
        table = dict_to_table(d)
        print(tabulate(table, tablefmt="plain"))
        if idx < len(data) - 1:
            print("\n")

def urlscan_domain_api(domain):
    url = "https://urlscan.io/api/v1/search/"
    params = {"q": domain}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        pydata=json.loads(response.text)
        for i in elements_list:
            if i in pydata:
                print(i," : ",pydata[i])
        results=pydata["results"]
        print("\nResults : \n")
        print_dict_table(results)
    else:
        print("Error:", response.status_code)
    


