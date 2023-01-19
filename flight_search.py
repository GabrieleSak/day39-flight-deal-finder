# This class is responsible for talking to the Flight Search API.

import requests
from auth import tequila_api_key

TEQUILA_API_KEY = tequila_api_key


class FlightSearch:
    def __init__(self, params):
        self.headers = {"apikey": TEQUILA_API_KEY}
        self.parameters = params
        self.tequila_endpoint = f"https://api.tequila.kiwi.com/v2/search"
        self.flight_responses = []

    def flight_search(self):
        for param in self.parameters:
            flight_response = requests.get(self.tequila_endpoint, params=param, headers=self.headers)
            self.flight_responses.append(flight_response.json())
        return self.flight_responses
