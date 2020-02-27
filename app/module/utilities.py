# -*- coding: utf-8 -*-
import json
import pytz


class Utilities:
    @staticmethod
    def json_loader(path: str) -> list:
        with open(path, "r") as data_file:
            json_data = data_file.read()
        return json.loads(json_data)

    @staticmethod
    def json_writer(data: list, path: str) -> list:
        try:
            with open(path, "w") as outfile:
                json.dump(data, outfile)
        except:
            restart()

    @staticmethod
    def is_valid_timezone(tz: str) -> bool:
        tz_list = pytz.all_timezones
        if tz in tz_list:
            return True
        return False

    @staticmethod
    def print_error_message(message: str) -> None:
        print("Error: {}".format(message))

    @staticmethod
    def is_blank(s: str) -> bool:
        return not bool(s and s.strip())
