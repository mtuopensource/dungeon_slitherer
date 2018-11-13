import json

def readConfig(filename):
    data = {}
    with open(filename) as json_file:
        data = json.load(json_file)
    return data