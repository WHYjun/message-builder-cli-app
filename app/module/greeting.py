# -*- coding: utf-8 -*-
from datetime import datetime
from .component import Component
from .utilities import Utilities


class Greeting(Component):
    def __init__(self):
        self.id = None
        self.timezone = None
        self.component = None
        self.component_list = None
        self.path = "./data/Greetings.json"

    def get_greeting(self) -> str:
        return self.component.get("text")

    def initialize_with_id(self, id: int, tz: datetime.tzinfo) -> object:
        self.id = id
        self.timezone = tz
        greeting_json_list = self.get_list()
        for greeting_json in greeting_json_list:
            if greeting_json.get("id") == id:
                self.component = self.get_expression(id, tz)
        return self

    def initialize_with_user_input(self, tz: datetime.tzinfo) -> int:
        print("Oh! The template you chose has greeting.")
        print("Which greeting do you want to add to message?")
        self.print_list()
        try:
            greeting_id = int(input("Type ID: "))
        except:
            Utilities.print_error_message("Wrong Input. ID should be integer.")
        return self.initialize_with_id(greeting_id, tz)

    def print_list(self) -> None:
        greeting_list = self.get_list()
        for greeting in greeting_list:
            print(greeting.get("id"), greeting.get("type"))

    def get_expression(self, id: int, tz: datetime.tzinfo) -> dict:
        current_time = datetime.now(tz=tz)
        greeting_list = self.get_list()

        for greeting in greeting_list:
            if id == greeting.get("id"):
                exp_list = greeting.get("expression")
                for exp in exp_list:
                    if exp.get("startHour") <= current_time.hour and current_time.hour <= exp.get("endHour"):
                        return exp
        return None

    def save(self, args: dict):
        pass
