# -*- coding: utf-8 -*-
from datetime import datetime as dt
from .greeting import Greeting
from .template import Template
from tzlocal import get_localzone
import pytz
from .utilities import Utilities


class Message:
    def __init__(self, template: Template) -> None:
        self.placeholders = template.placeholders
        self.body = template.get_message()
        self.timezone = get_localzone()

    def populate(self, obj: object) -> None:
        # iterate keys except id and replace placeholders with keys
        data = obj.get_data()
        body = self.body
        for key in data.keys():
            val = data.get(key)
            if Utilities.is_blank(str(val)):
                Utilities.print_error_message(
                    "{} data is empty. Please check json file.".format(key))
            if key is "timezone" and Utilities.is_valid_timezone(tz):
                self.timezone = pytz.timezone(val)
            if isinstance(val, dt):
                val = self.timezone.localize(val).astimezone()
                val = val.strftime("%m/%d/%Y, %H:%M:%S")
            if key in self.placeholders.keys():
                placeholder = self.placeholders.get(key)
                body = body.replace(placeholder, val)
        self.body = body

    def add_greeting(self) -> None:
        body = self.body
        place_holder = self.placeholders.get("greeting")
        if place_holder in body:
            greeting = Greeting().initialize_with_user_input(self.timezone)
            body = body.replace(place_holder, greeting.get_greeting())

        self.body = body
