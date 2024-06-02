import requests
import json
from rich import print
from tabulate import tabulate
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("ABUSEIPDB_API_KEY")



def abuseipdb_ip_api(ip_address):
    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }
    response = requests.get(url=url, headers=headers, params=querystring)
    pydata=json.loads(response.text)
    
    if "data" in pydata:
        data=pydata["data"]
                # Flatten the dictionary except 'hostnames'
        flat_response = {k: v if k == 'hostnames' else [v] for k, v in data.items()}

        # Tabulate 'hostnames' as a separate table if it's a list
        if isinstance(flat_response['hostnames'], list):
            hostnames = flat_response.pop('hostnames')
            hostnames_table = tabulate(hostnames, headers=['Hostname'], tablefmt='grid')
            print('Hostnames:')
            print(hostnames_table)

        # Tabulate the rest of the flattened dictionary
        print('\nOther Information:')
        headers = ['Key', 'Value']
        rows = [[k, v[0]] for k, v in flat_response.items()]
        print(tabulate(rows, headers=headers, tablefmt='grid'))


