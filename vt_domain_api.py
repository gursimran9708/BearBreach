import requests
import json
from tabulate import tabulate
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("VT_API_KEY")

elements_list = [

        "creation_date",
        "jarm",
        "last_analysis_date",
        "last_dns_records_date",
        #"last_https_certificate",
        "last_https_certificate_date",
        "last_modification_date",
        "last_update_date",
        #"popularity_ranks",
        "registrar",
        "reputation",
        "tags",
        #"total_votes",
        "whois",
        "whois_date"
    ]      

def vt_domain_api(domain):
    url=f"https://www.virustotal.com/api/v3/domains/{domain}"
    response=requests.get(url,headers={"X-Apikey":api_key})
    py_data=json.loads(response.text)
    
    
    
    if "data" in py_data:
            if "attributes" in py_data["data"]:
                for key in elements_list:
                    if f"{key}" in py_data["data"]["attributes"]:
                        print(f"{key} : ",py_data["data"]["attributes"][key])

    if "data" in py_data:
        if "attributes" in py_data["data"]:
            if "categories" in py_data["data"]["attributes"]:
                data=py_data["data"]["attributes"]["categories"]
                # Convert dictionary to list of lists
                table = []
                for key, value in data.items():
                    table.append([key, value])

                # Print table
                print(tabulate(table, headers=["Tool", "Verdict"], tablefmt="grid"))
                
                
            if "total_votes" in py_data["data"]["attributes"]:
                data=py_data["data"]["attributes"]["total_votes"]
                # Convert dictionary to list of lists
                table = []
                for key, value in data.items():
                    table.append([key, value])

                # Print table
                print(tabulate(table, headers=["Harmless", "Malicious"], tablefmt="grid"))


    
     
            if  "last_analysis_stats" in py_data["data"]["attributes"]:
                last_analysis_stats=py_data["data"]["attributes"]["last_analysis_stats"]
                table_data = [[key, value] for key, value in last_analysis_stats.items()]

# Print the table
                print(tabulate(table_data, headers=["Category", "Count"], tablefmt="grid"))

    last_dns_records = py_data["data"]["attributes"]["last_dns_records"]
    headers = set().union(*(d.keys() for d in last_dns_records))
    table_data = [[d.get(header, '') for header in headers] for d in last_dns_records]                       
    print(tabulate(table_data, headers=headers, tablefmt="grid"))    


    if "last_analysis_results" in py_data["data"]["attributes"]:
        data=py_data["data"]["attributes"]["last_analysis_results"]
        table_data = [[key, value['method'], value['category'], value['result']] for key, value in data.items()]

                # Define the headers
        headers = ["Engine Name", "Method", "Category", "Result"]

                # Print the table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

