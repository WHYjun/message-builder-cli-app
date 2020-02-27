# -*- coding: utf-8 -*-
from datetime import datetime
from .message import Message
from .utilities import Utilities
from pytz import timezone


class MessageBuilder:
    def __init__(self, template) -> None:
        self.message = Message(template)
        self.reset()

    def reset(self) -> None:
        self.template = None

    def build(self) -> Message:
        self.message.add_greeting()
        message = self.message
        self.reset()
        return message       

    def populate_guest(self, guest: object) -> object:
        self.message.populate(guest)
        return self

    def populate_company(self, company: object) -> object:
        self.message.populate(company)
        return self

    def populate_reservation(self, reservation: object) -> object:
        self.message.populate(reservation)
        return self

    def check_placeholder(self, message: object) -> bool:
        text = message.body
        if "[[" in text or "]]" in text:
            print("Your message still have double brackets. Is it okay to send this message to user?")
            print(text)
            user_input = input("Type Y or N")
            if user_input.upper() == "N":
                Utilities.print_error_message("Please check your template.")
                raise      