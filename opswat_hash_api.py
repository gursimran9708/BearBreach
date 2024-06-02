import requests
import json
from tabulate import tabulate
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("OPSWAT_API_KEY")

elements_list=[
    'scan_result_history_length',
    'sandbox',
    'file_id',
    'data_id',
    #'process_info',
    #'scan_results',
    #'file_info',
    'share_file',
    'rest_version',
    'additional_info',
    'votes',
    'stored'
]

    

def opswatmetadefender_api_files(x):
    url=f"https://api.metadefender.com/v4/hash/{x}"
    
    result=requests.get(url,headers={"apikey":api_key})
    pyresult=json.loads(result.text)
    for i in pyresult:
        if i in elements_list:
            print(f"{i} : {pyresult[i]} \n")
        
        
        if i=="scan_results":
            scan_results=pyresult["scan_results"]
            headers = ["Antivirus", "Threat Found", "Scan Time", "Scan Result", "Definition Time"]

            table = []
            for av, details in scan_results['scan_details'].items():
                threat_found = details['threat_found'] if details['threat_found'] else 'No threat found'
                scan_time = details['scan_time']
                scan_result = 'Infected' if details['scan_result_i'] == 1 else 'Clean'
                definition_time = details['def_time']
                table.append([av, threat_found, scan_time, scan_result, definition_time])

            print("\nScan Results : \n",tabulate(table, headers=headers,tablefmt="grid"))
    
        if i=="file_info":
            file_info=pyresult["file_info"]
            headers = ["Attribute", "Value"]

            table = []
            for attribute, value in file_info.items():
                table.append([attribute, value])

            print("\nFile Info. : \n",tabulate(table, headers=headers,tablefmt="grid"))
    
        if i=="process_info":
            process_info=pyresult["process_info"]
            headers = ["Attribute", "Value"]

            table = []
            for attribute, value in process_info.items():
                table.append([attribute, value])

            print("\nProcess Info. : \n",tabulate(table, headers=headers,tablefmt="grid"))
    
        if i=="votes":
            votes=pyresult["votes"]
            
            if 'votes' in votes:
                table = [["Attribute", "Value"],
                        ["Upvotes", votes["votes"].get("up", 0)],
                        ["Downvotes", votes["votes"].get("down", 0)]]
            else:
                table = [["Attribute", "Value"],
                        ["Upvotes", 0],
                        ["Downvotes", 0]]

            print("\nVotes : \n",tabulate(table, headers="firstrow",tablefmt="grid"))
            
