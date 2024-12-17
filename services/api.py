import os
import requests


BASE_URL = os.getenv("BACKEND_URL")

def get_quote_by_id(quote_id):
    try:
        response = requests.get(f"{BASE_URL}/quotes/{quote_id}")
        if response.status_code == 200:
            return response.json()
        return []
    
    except Exception as e:
        print(e)
        return []