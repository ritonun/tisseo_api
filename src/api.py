import requests

class TisseoAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = ""
