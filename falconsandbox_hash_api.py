import requests 
import json
from rich import print
from tabulate import tabulate 
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("FALCON_API_KEY")
elements_list=[
    'sha256',
    'last_file_name',
    'other_file_name',
    'threat_score',
    'verdict',
    'url_analysis',
    'size',
    'type',
    'type_short',
    'analysis_start_time',
    'last_multi_scan',
    'tags',
    'architecture',
    'vx_family',
    'multiscan_result',
    #'scanners',
    #'scanners_v2',
    'submit_context',
    'related_parent_hashes',
    'related_children_hashes',
    'reports',
    'whitelisted',
    'children_in_queue',
    'children_in_progress',
    'related_reports'
]

def falcon_api_files(x):
    url=f"https://www.hybrid-analysis.com/api/v2/overview/{x}"
    result=requests.get(url=url, headers={"api-key":api_key})
    pyresult=json.loads(result.text)
    for i in pyresult:
        if i in elements_list:
            print(f"\n{i} : {pyresult[i]}")

        if i=="scanners":
            scanners=pyresult["scanners"]
            headers = ["Name", "Status", "Error Message", "Progress", "Total", "Positives", "Percent", "Anti-Virus Results"]

            table = [[d["name"], d["status"], d["error_message"], d["progress"], d["total"], d["positives"], d["percent"], d["anti_virus_results"]] for d in scanners]

            print("\nscanners : \n\n",tabulate(table, headers=headers,tablefmt="grid"))

        if i=="scanners_v2":
            scanners_v2=pyresult["scanners_v2"]
            headers = ["Name", "Status", "Error Message", "Progress", "Total", "Positives", "Percent", "Anti-Virus Results"]

            table = []
            for key, value in scanners_v2.items():
                if value is None:
                    table.append([key, "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"])
                else:
                    table.append([value.get("name", "N/A"), value.get("status", "N/A"), value.get("error_message", "N/A"), value.get("progress", "N/A"), value.get("total", "N/A"), value.get("positives", "N/A"), value.get("percent", "N/A"), value.get("anti_virus_results", "N/A")])

            print("\nscanners_v2 : \n\n",tabulate(table, headers=headers,tablefmt="grid",))
            
    
#falcon_api_files("06b7a77450ca6c17378b702c4dd49abbd768f59b6666812fe1cd1ce4d231a6bb") 
    
