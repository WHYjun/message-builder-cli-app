# -*- coding: utf-8 -*-
from .component import Component
from .utilities import Utilities


class Company(Component):
    def __init__(self):
        self.id = None
        self.component = None
        self.component_list = None
        self.path = "./data/Companies.json"

    def initialize_with_user_input(self) -> object:
        print("Which company do you want to send a message from?")
        self.print_list()
        try:
            company_id = int(input("Type ID: "))
        except:
            Utilities.print_error_message("Wrong Input. ID should be integer")
        return self.initialize_with_id(company_id)

    def print_list(self) -> None:
        company_list = self.get_list()
        for company in company_list:
            if company.get("id") > 0:
                print(company.get("id"), company.get("company"))

    def save(self, new_data: dict) -> None:
        pass
