# -*- coding: utf-8 -*-
from .component import Component
from .reservation import Reservation
from .utilities import Utilities


class Guest(Component):
    def __init__(self):
        self.id = None
        self.component = None
        self.component_list = None
        self.reservation = None
        self.path = "./data/Guests.json"

    def initialize_with_id(self, id: int) -> object:
        self.id = id
        if id > 0:
            guest_json_list = self.get_list()
            for guest_json in guest_json_list:
                if guest_json.get("id") == id:
                    self.component = guest_json
                    self.reservation = Reservation(guest_json)
                    return self
        Utilities.print_error_message("Typed id is not existed.")
        raise

    def initialize_with_user_input(self) -> int:
        print("Which guest do you want to send a message?")
        self.print_list()
        try:
            guest_id = int(input("Type ID: "))
        except:
            Utilities.print_error_message("Wrong Input. ID should be integer")
            raise
        return self.initialize_with_id(guest_id)

    def get_reservation(self) -> object:
        return self.reservation

    def print_list(self) -> None:
        guest_list = self.get_list()
        for guest in guest_list:
            if guest.get("id") > 0:
                print(guest.get("id"), guest.get("firstName"),
                    guest.get("reservation").get("roomNumber"))

    def save(self, new_data: dict) -> None:
        pass
