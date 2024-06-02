from polyswarm_api.api import PolyswarmAPI
from rich import print
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("POLYSWARM_API_KEY")

def polyswarm_api_files(x):
    community_name = "default"
    try:
        api = PolyswarmAPI(key=api_key, community=community_name)
        results = api.search(x)
        positives = 0
        total = 0

        for result in results:
            if result.failed:
                print(f'Failed to get result.')
                break

            if not result.assertions:
                print('Artifact not scanned yet - Run rescan for Engine Assertions.')
            else:
                print('Engine Assertions:')
                for assertion in result.assertions:
                    if assertion.verdict:
                        positives += 1
                    total += 1
                    print('\tEngine {} asserts {}'. \
                          format(assertion.author_name,
                                 'Malicious' if assertion.verdict else 'Benign'))

            print(f'Positives: {positives}')
            print(f'Total: {total}')
            print(f'PolyScore: {result.polyscore}\n')

            print(f'sha256: {result.sha256}')
            print(f'sha1: {result.sha1}')
            print(f'md5: {result.md5}')
            print(f'Extended type: {result.extended_type}')
            print(f'First Seen: {result.first_seen}')
            print(f'Last Seen: {result.last_seen}\n')

            print(f'Permalink: {result.permalink}')

    except Exception:
        print(f'No results for the provided hash.')


