import json
from pprint import pprint

with open("chap5/test2.json", mode="r") as f:
    jsondata = json.loads(f.read())
    pprint(jsondata)
    