from Serviceable import Serviceable
from abc import ABC, abstractmethod

class Battery(Serviceable, ABC):
    @abstractmethod
    def needs_service(self):
        pass