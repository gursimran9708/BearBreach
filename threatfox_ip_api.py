import requests
import json
from tabulate import tabulate
from rich import print
def threatfox_ip_api(ip):
    url = "https://threatfox-api.abuse.ch/api/v1/"
    data = {
        "query": "search_ioc",
        "search_term": ip
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        try:
            pydata = response.json()  # Parse JSON response
            if "data" in pydata:
                data = pydata["data"]
                if isinstance(data, dict):  # Check if data is a dictionary
                    # Convert dictionary to list of lists for tabulate
                    rows = [[k, v] for k, v in data.items()]
                    print(tabulate(rows, tablefmt="pretty"))
                elif isinstance(data, list):  # Check if data is a list of dictionaries
                    # Convert list of dictionaries to list of lists for tabulate
                    rows = [[k, v] for d in data for k, v in d.items()]
                    print(tabulate(rows, tablefmt="pretty"))
                else:
                    print("Unexpected data format:", type(data))
        except json.JSONDecodeError:
            print("Error decoding JSON response")
    else:
        print("Error:", response.status_code)

