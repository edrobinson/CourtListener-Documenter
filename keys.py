'''
Testing the idea of a glossary from a json file
'''
import json


def get_all_unique_keys(data):
    keys = []
    if isinstance(data, dict):
        for key, value in data.items():
            keys.append(key)
            keys.extend(get_all_keys(value))
    elif isinstance(data, list):
        for item in data:
            keys.extend(get_all_keys(item))
    
    unique_values = list(dict.fromkeys(keys))
    return unique_values
    
f = open('ClApiJson/clusters.json', 'r')
sJson = f.read()
f.close()
jdict = json.loads(sJson)
#Iterative scan over the API json for key values
keys = get_all_unique_keys(jdict)
#Lower case each one
keys = [item.lower() for item in keys]
#Sort them
keys.sort()




