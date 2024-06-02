import requests
import json
from tabulate import tabulate
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("OPSWAT_API_KEY")


def opswat_domain_api(domain):
    url = f"https://api.metadefender.com/v4/domain/{domain}"
    headers = {
    "apikey": api_key
    }   
    response = requests.get(url, headers=headers)
    pydata=json.loads(response.text) 
    if "address" in pydata:
        print("Address : ",pydata["address"],"\n")
    if "lookup_results" in pydata:
        lookup_results=pydata["lookup_results"]
        sources_table = [[source.get('provider', ''), source.get('assessment', ''), source.get('category', ''),
                  source.get('detect_time', ''), source.get('update_time', ''), source.get('status', '')]
                 for source in lookup_results['sources']]

        # Create table header
        header = ['provider', 'assessment', 'category', 'detect_time', 'update_time', 'status']

        # Insert a blank line between every dictionary
        table = [['', '', '', '', '', '']] + sources_table

        # Tabulate the data
        print(tabulate([
            ('start_time', lookup_results.get('start_time', '')),
            ('detected_by', lookup_results.get('detected_by', '')),
            ('sources', tabulate(table, headers=header, tablefmt='grid'))
        ], tablefmt='grid'))



