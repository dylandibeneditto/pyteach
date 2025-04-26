import os
import json

def load_challenges():
    f = open(os.path.join(os.path.dirname(__file__), "challenges.json"), 'r')
    data = json.load(f)

    return data["challenges"]

def add_completion(cid: str):
    f = open(os.path.join(os.path.dirname(__file__), "data.json"), 'r')
    data = json.load(f)

    if cid not in data["completed"]:
        data["completed"].append(cid)

    with open(os.path.join(os.path.dirname(__file__), "data.json"), 'w') as f:
        json.dump(data, f, indent=4)

def is_completed(cid: str) -> bool:
    f = open(os.path.join(os.path.dirname(__file__), "data.json"), 'r')
    data = json.load(f)

    return cid in data["completed"]
    