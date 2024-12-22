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
class getApiJsons:
    # headers array for requests
    Headers = {"Authentication": "Token your cl auth token"}
    
    def __init__(self, outputFolder):
        self.outputFolder = outputFolder
        self.count = 0


    # Make a pretty formatted string of a json string
    def prettyJson(self,str):
        d = json.loads(str)
        pretty = json.dumps(d, indent=4)
        return pretty


    # Fetch the APIs
    def getTheApiUrls(self):

        r = requests.get("https://www.courtlistener.com/api/rest/v4/", headers=self.Headers)
        if r.status_code != 200:
            exit(
                f"API urls requests failed with status code {r.status_code}. Terminating.\n "
            )
        data = r.json()
        return data


    # Retrieve an API,s OPTIONS
    def getAnApiOptions(self,api, url):
        r = requests.options(url, headers=self.Headers)
        if r.status_code != 200:
            print(f"{api} request failed with code {r.status_code}")
            return False
        return r.text


    # Do it . . .
    def process(self):
        apiList = self.getTheApiUrls()
        for api, url in apiList.items():
            # Get the next API's options json
            json = self.getAnApiOptions(api, url)
            if json == False:
                continue

            json = self.prettyJson(json)
            path = f"{self.outputFolder}/{api}.json"
            f = open(path, "w")
            f.write(json)
            f.close
            self.count +=1
        print(f"Done. Created {self.count} API JSON files.")
