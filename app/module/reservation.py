# -*- coding: utf-8 -*-
from datetime import datetime as dt
from pytz import utc


class Reservation:
    def __init__(self, guest: dict):
        self.reservation = guest.get("reservation")

    def get_data(self) -> dict:
        reservation = {
            "roomNumber": str(self.reservation.get("roomNumber")),
            "startTimestamp": dt.fromtimestamp(self.reservation.get("startTimestamp")),
            "endTimestamp": dt.fromtimestamp(self.reservation.get("endTimestamp"))
        }
        return reservation
