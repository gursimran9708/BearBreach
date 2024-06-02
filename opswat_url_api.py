import requests
import json
from urllib.parse import quote
from tabulate import tabulate
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("OPSWAT_API_KEY")


def encode_url(normal_url):
    encoded_url = quote(normal_url,safe='')
    return encoded_url

#print(encode_url("http://hdfc.pp.ru/permit/gate.php"))

def opswatmetadefender_url_api(url_to_query):
    url_to_query=encode_url(url_to_query)
    url=f"https://api.metadefender.com/v4/url/{url_to_query}"
    api_key="a7c966d72a13ac3a6e23b7e7ae67bbd6"
    response=requests.get(url,headers={"apikey":api_key})
    
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
        

