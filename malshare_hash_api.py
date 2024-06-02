import requests
import json
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("MALSHARE_API_KEY")

elements_list=['MD5', 'SHA1', 'SHA256', 'SSDEEP', 'F_TYPE', 'FILENAMES']
def malshare_api_files(x):
  
   result=requests.get(url= f"https://malshare.com/api.php?api_key={api_key}&action=details&hash={x}")
   info=result.text
   pyresult=json.loads(info)
   for i in pyresult:
      if i in elements_list:
         print(i," : ",pyresult[i])
         
        
