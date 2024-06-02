from polyswarm_api.api import PolyswarmAPI
import sys
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("POLYSWARM_API_KEY")


community_name = "default"
api = PolyswarmAPI(key=api_key, community=community_name)

def polyswarm_url_api(url):
    positives = 0
    total = 0

    instance = api.submit(url, artifact_type='url')
    result = api.wait_for(instance)

    if result.failed:
        print(f'Failed to get results')
        sys.exit()

    print('Engine Assertions:')
    for assertion in result.assertions:
        if assertion.verdict:
            positives += 1
        total += 1
        print('\tEngine {} asserts {}'.\
            format(assertion.author_name,
                   'Malicious' if assertion.verdict else 'Benign'))

    print(f'Positives: {positives}')
    print(f'Total: {total}\n')

    print(f'Permalink: {result.permalink}')
    
