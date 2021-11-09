# UTils
import json

def j(string):
    return json.dumps(string)

def s(obj):
    return json.dumps(json.dumps(obj))

