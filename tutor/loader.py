import os
import json

def load_challenges():
    f = open(os.path.join(os.path.dirname(__file__), "challenges.json"), 'r')
    data = json.load(f)

    return data["challenges"]
    