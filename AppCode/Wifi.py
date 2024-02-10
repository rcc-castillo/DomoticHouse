import requests
class Wifi:
    def __init__(self, server_url):
        self.SERVER_URL = server_url
        self.connected = False

    def post(self, endpoint, data):
        url = self.SERVER_URL + endpoint
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        try:
            response = requests.post(url, headers=headers, data=data, timeout=2)
        except requests.exceptions.Timeout:
            print("Timeout occurred")
            return

        if response.status_code == 200:
            print(f"{response.status_code}:  {response.text}")
        else:
            print(f"[ERROR] {response.status_code}:  {response.text}")

    def get(self, endpoint):
        url = self.SERVER_URL + endpoint
        try:
            response = requests.get(url, timeout=2)
        except requests.exceptions.Timeout:
            print("Timeout occurred")
            return None
        
        if response.status_code == 200:
            print(f"{response.status_code}:  {response.text}")
            return response.json()
        else:
            print(f"[ERROR] {response.status_code}:  {response.text}")
            return None
    
    def connect(self):
        self.connected = True
    
    def disconnect(self):
        self.connected = False

    def isConnected(self):
        return self.connected