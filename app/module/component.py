# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from .utilities import Utilities


class Component(ABC):
    @abstractmethod
    def __init__(self):
        self.id = None
        self.component = None
        self.component_list = None
        self.path = None

    def initialize_with_id(self, id: int) -> object:
        self.id = id
        if id > 0:
            data_list = self.get_list()
            for data in data_list:
                if data.get("id") == id:
                    self.component = data
                    return self
        Utilities.print_error_message("Typed_id is not existed.")

    @abstractmethod
    def initialize_with_user_input(self) -> int:
        pass

    def get_data(self) -> dict:
        return self.component

    def get_list(self) -> list:
        if self.component_list is None:
            self.component_list = Utilities.json_loader(self.path)
        return self.component_list

    @abstractmethod
    def print_list(self) -> None:
        pass

    @abstractmethod
    def save(self, new_data: dict) -> None:
        pass
