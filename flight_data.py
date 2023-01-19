# This class is responsible for structuring the flight data.

import iso8601


class FlightData:
    def __init__(self, search_data):
        self.price = search_data["price"]
        self.from_city = search_data["cityFrom"]
        self.from_code = search_data["flyFrom"]
        self.to_city = search_data["cityTo"]
        self.to_code = search_data["flyTo"]
        self.outbound_date = iso8601.parse_date(search_data["route"][0]["local_departure"]).strftime('%Y-%m-%d')
        self.inbound_date = iso8601.parse_date(search_data["route"][-1]["local_departure"]).strftime('%Y-%m-%d')
        self.url = search_data["deep_link"]
