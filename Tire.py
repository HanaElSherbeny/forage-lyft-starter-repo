from Serviceable import Serviceable
from abc import ABC, abstractmethod

class Tire(Serviceable, ABC):
    @abstractmethod
    def needs_service(self):
        pass