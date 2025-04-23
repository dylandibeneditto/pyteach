import os
import json

def load_challenge(name):
    folder = os.path.join("challenges", name)
    try:
        with open(os.path.join(folder, "meta.json")) as f:
            meta = json.load(f)
        with open(os.path.join(folder, "solution.py")) as f:
            user_code = f.read()
        meta["user_code"] = user_code
        return meta
    except Exception as e:
        print(f"Error loading challenge '{name}': {e}")
        return None