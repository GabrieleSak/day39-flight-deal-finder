# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

data_manager = DataManager()
flight_search_parameters = data_manager.get_params_for_api()

flight_search = FlightSearch(flight_search_parameters)
flight_search_data = flight_search.flight_search()

for data in flight_search_data:
    if data["data"]:
        flight_info = FlightData(data["data"][0])
        notification_manager = NotificationManager(flight_info)
        notification_manager.send_email()
