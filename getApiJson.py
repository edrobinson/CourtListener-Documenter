import json
import requests
import utils

"""
This script builds a folder full of the CourtListener APIs
HTTP OPTIONS responses. The purpose is to provide
an offline data source for the page generation class use to
generate the documentation from.
The output islocated in /ClApiJson
"""
# headers array for requests
aHeaders = {"Authentication": "Token 2ce053ed5100cd5b3d3486ea51711be2915ad8c5"}


# Make a pretty formatted string of a json string
def prettyJson(str):
    d = json.loads(str)
    pretty = json.dumps(d, indent=4)
    return pretty


# Do a get on the CL rest API base url to get the list of name : url
def loadTheApiUrls():

    r = requests.get("https://www.courtlistener.com/api/rest/v4/", headers=aHeaders)
    if r.status_code != 200:
        exit(
            f"API urls requests failed with status code {r.status_code}. Terminating.\n "
        )
    data = r.json()
    return data


# Retrieve an API,s OPTIONS
def getAnApiOptions(api, url):
    r = requests.options(url, headers=aHeaders)
    if r.status_code != 200:
        print(f"{api} request failed with code {r.status_code}")
        return False
    return r.text


# Do it . . .
def process():
    apiList = loadTheApiUrls()
    for api, url in apiList.items():
        # Get the next API's options json
        json = getAnApiOptions(api, url)
        if json == False:
            continue

        json = prettyJson(json)
        path = f"ClApiJson/{api}.json"
        f = open(path, "w")
        f.write(json)
        f.close

        #print(f"Created {path}")
    print(f"Done . . .")


# Do it
process()
