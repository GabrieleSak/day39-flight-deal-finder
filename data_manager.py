# This class is responsible for talking to the Google Sheet.

import requests as requests
from auth import *
from datetime import datetime, timedelta

SHEET_USERNAME = sheet_username
PROJECT_NAME = projectName
SHEET_NAME = sheetName
SHEET_TOKEN = sheet_token
FLY_FORM = "VNO"


class DataManager:
    def __init__(self):
        self.sheet_endpoint = f"https://api.sheety.co/{SHEET_USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
        self.sheet_headers = {"Authorization": f"Bearer {SHEET_TOKEN}"}
        self.flight_search_parameters = []

    def get_sheet_data(self):
        sheet_response = requests.get(self.sheet_endpoint, headers=self.sheet_headers)
        return sheet_response.json()["prices"]

    def get_params_for_api(self):
        today = datetime.now()
        today_plus_6_month = today + timedelta(days=180)
        data = self.get_sheet_data()
        for row in data:
            data_dict = dict(
                fly_from=FLY_FORM,
                fly_to=row["iataCode"],
                date_from=today.strftime("%d/%m/%Y"),
                date_to=today_plus_6_month.strftime("%d/%m/%Y"),
                flight_type="round",
                nights_in_dst_from=1,
                nights_in_dst_to=30,
                limit=1,
                price_to=row["lowestPrice"]
            )
            self.flight_search_parameters.append(data_dict)
        return self.flight_search_parameters

