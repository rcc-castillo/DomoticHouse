import requests
class Wifi:
    def __init__(self, server_url):
        self.SERVER_URL = server_url

    def post(self, endpoint, data):
        """
        Sends the data to the wifi
        """
        url = self.SERVER_URL + endpoint
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print(f"{response.status_code}:  {response.text}")
        else:
            print(f"[ERROR] {response.status_code}:  {response.text}")

    def get(self, endpoint):
        """
        Reads the data from the wifi
        """
        url = self.SERVER_URL + endpoint
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{response.status_code}:  {response.text}")
            return response.json()
        else:
            print(f"[ERROR] {response.status_code}:  {response.text}")
            return None