# This class is responsible for sending notifications with the deal flight details.
import smtplib
from auth import *


class NotificationManager:
    def __init__(self, flight_data):
        self.my_email = my_email
        self.email = email
        self.password = password
        self.price = flight_data.price
        self.from_city = flight_data.from_city
        self.from_code = flight_data.from_code
        self.to_city = flight_data.to_city
        self.to_code = flight_data.to_code
        self.outbound_date = flight_data.outbound_date
        self.inbound_date = flight_data.inbound_date
        self.url = flight_data.url

    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Low price alert! Flight to {self.to_city} \n\n Only {self.price}€ to fly from "
                    f"{self.from_city}-{self.from_code} to {self.to_city}-{self.to_code}, "
                    f"from {self.outbound_date} to {self.inbound_date}\n\n\n{self.url}".encode("utf-8")
            )
