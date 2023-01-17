import requests as requests
from auth import sheet_username, projectName, sheetName, sheet_token

SHEET_USERNAME = sheet_username
PROJECT_NAME = projectName
SHEET_NAME = sheetName
SHEET_TOKEN = sheet_token


class DataManager:
    def __init__(self):
        self.sheet_endpoint = f"https://api.sheety.co/{SHEET_USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
        self.sheet_headers = {"Authorization": f"Bearer {SHEET_TOKEN}"}

    def get_flight_data(self):
        sheet_response = requests.get(self.sheet_endpoint, headers=self.sheet_headers)
        return sheet_response.json()
