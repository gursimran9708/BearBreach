import requests
import json
from tabulate import tabulate
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("VT_API_KEY")


    
    
element_list=['tlsh', 
              'capabilities_tags',
              'creation_date',
              'downloadable',
              'sandbox_verdicts',
              'first_submission_date',
             'last_analysis_date',
             #'type_tags',
             'times_submitted',
             'type_description',
             #'total_votes',
             'authentihash',
             'first_seen_itw_date',
             #'last_analysis_stats',
             'sha1',
             'type_extension',
             #'signature_info',
             'last_submission_date',
             'sha256',
             #'tags',
             'magic',
             #'trid',
             'unique_sources',
             'vhash',
             #'names',
             'reputation', 
             'meaningful_name', 
             #'pe_info',
             #'last_analysis_results',
             'ssdeep',
             'creation_date',
             #'detectiteasy',
             'last_modification_date',
             'md5',
             'type_tag',
             'size',
             'crowdsourced_ai_results']

def vt_api_files(x):
    
    url = f"https://www.virustotal.com/api/v3/files/{x}"
    response = requests.get(url, headers={"X-Apikey": api_key, "accept": "application/json"})
    pydata=json.loads(response.text)
    
    if "data" in pydata:
        if "attributes" in pydata["data"]:
            for key in element_list:
                if key in pydata["data"]["attributes"]:
                    print(f"{key} : ",pydata["data"]["attributes"][key],"\n")
    
            if "type_tags" in pydata["data"]["attributes"]:
                print("Type Tags : \n")
                type_tags=pydata["data"]["attributes"]["type_tags"]
                for i in type_tags:
                    print(i)

            if "total_votes" in pydata["data"]["attributes"]:
                print("\nTotal Votes : \n")
                total_votes=pydata["data"]["attributes"]["total_votes"]
                print(tabulate(total_votes.items(), headers=["Category", "Count"], tablefmt="grid"))
            
            if "last_analysis_stats" in pydata["data"]["attributes"]:
                print("\nLast Analysis Stats : \n")
                last_analysis_stats=pydata["data"]["attributes"]["last_analysis_stats"]
                print(tabulate(last_analysis_stats.items(), headers=["Category", "Count"], tablefmt="grid"))

            if "tags" in pydata["data"]["attributes"]:
                tags=pydata["data"]["attributes"]["tags"]
                print("\nTags : \n")
                for i in tags: 
                    print(i)
                    
            if "trid" in pydata["data"]["attributes"]:
                print("\nTRID : \n")
                trid=pydata["data"]["attributes"]["trid"]
                print(tabulate(trid, headers="keys", tablefmt="grid"))
                
            if "names" in pydata["data"]["attributes"]:
                names=pydata["data"]["attributes"]["names"]
                print("\nNames : \n")
                for i in names: 
                    print(i)
               
            if "pe_info" in pydata["data"]["attributes"]:
                pe_info=pydata["data"]["attributes"]["pe_info"]
                resource_details = pe_info.get('resource_details', [])
                print("\npe_info : \n")
                resource_details_data = [[rd.get('lang', ''), rd.get('chi2', ''), rd.get('filetype', ''), rd.get('entropy', ''), rd.get('sha256', ''), rd.get('type', '')] for rd in resource_details]
                # Tabulate resource details
                print(tabulate(resource_details_data, headers=["Language", "Chi2", "File Type", "Entropy", "SHA256", "Type"], tablefmt="grid"))
             
            if "last_analysis_results" in pydata["data"]["attributes"]:
                last_analysis_results=pydata["data"]["attributes"]["last_analysis_results"]  
                print("\nLast Analysis Results : \n")
                table_data = []
                for engine, info in last_analysis_results.items():
                    table_data.append([engine, info['method'], info['engine_version'], info['engine_update'], info['category'], info['result']])

                # Tabulate the data
                print(tabulate(table_data, headers=["Engine", "Method", "Engine Version", "Engine Update", "Category", "Result"], tablefmt="grid"))
                            
            if "detectiteasy" in pydata["data"]["attributes"]:
                detectiteasy=pydata["data"]["attributes"]["detectiteasy"] 
                print("\ndetectiteasy : \n")
                table_data = []
                for value in detectiteasy['values']:
                    table_data.append([value.get('info', ''), value.get('version', ''), value.get('type', ''), value.get('name', '')])

                # Tabulate data
                print(tabulate(table_data, headers=["Info", "Version", "Type", "Name"], tablefmt="grid"))
                                       
                       
#vt_api_files("2d75cc1bf8e57872781f9cd04a529256")

def vt_api_files_json(x):
    url = f"https://www.virustotal.com/api/v3/files/{x}"
    response = requests.get(url, headers={"X-Apikey": api_key, "accept": "application/json"})
    return response
