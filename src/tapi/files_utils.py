import json


def save_json(data, path: str):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def load_json(path: str):
    with open(path, 'r') as f:
        return json.load(f)
