import requests
from config import API_URL

def extract_data():
    try:
        response = requests.get(API_URL, timeout=5)

        if(response.status_code == 200):
            return(response.json())
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Request failed: {e}")
        return None 