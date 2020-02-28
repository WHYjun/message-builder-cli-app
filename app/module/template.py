# -*- coding: utf-8 -*-
from .component import Component
from .utilities import Utilities


class Template(Component):
    def __init__(self):
        self.id = None
        self.component = None
        self.component_list = None
        self.path = "./data/Templates.json"
        self.placeholders = {
            "firstName": "[[guest_first_name]]",
            "lastName": "[[guest_last_name]]",
            "roomNumber": "[[reservation_room_number]]",
            "startTimestamp": "[[reservation_start_timestamp]]",
            "endTimestamp": "[[reservation_end_timestamp]]",
            "company": "[[company_name]]",
            "company_city": "[[company_city]]",
            "timezone": "[[company_timezone]]",
            "greeting": "[[greeting]]"
        }

    def initialize_with_user_input(self) -> object:
        print("Which template do you want to use?")
        print("If you want to create a new template, please type New")
        self.print_list()
        try:
            template_id = input("Type ID: ")
        except:
            Utilities.print_error_message("Wrong Input. ID should be integer")

        if template_id.lower() == "new":
            new_template = self.create_new_template()
            self.save(new_template)
            template_id = new_template.get("id")
        else:
            template_id = int(template_id)
        return self.initialize_with_id(template_id)

    def get_message(self) -> str:
        if self.component:
            return self.component.get("text")
        else:
            print("Template Object is not initialized yet.")
            return None

    def print_list(self) -> None:
        template_list = self.get_list()
        for template in template_list:
            if template.get("id") > 0:
                print(template.get("id"), template.get("title"))

    def create_new_template(self):
        temp_id = self.get_list()[-1].get("id") + 1
        temp_title = input("What's the title of template? Title is required.")
        if Utilities.is_blank(temp_title):
            Utilities.print_error_message("Template should have title.")
        self.print_placeholders()
        try:
            temp_text = input(
                "Type your template message here with using placeholders above:\n")
        except:
            Utilities.print_error_message("Input Error")

        if Utilities.is_blank(temp_text):
            Utilities.print_error_message("Template should have body message.")

        new_template = {
            "id": temp_id,
            "title": temp_title,
            "text": temp_text
        }
        return new_template

    def print_placeholders(self):
        for key in self.placeholders.keys():
            print("{}: {}".format(key, self.placeholders.get(key)))

    def save(self, new_data: dict) -> None:
        temp_list = self.get_list()
        temp_list.append(new_data)
        Utilities.json_writer(temp_list, self.path)
