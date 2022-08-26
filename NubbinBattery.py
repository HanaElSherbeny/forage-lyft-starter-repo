from Battery import Battery
from datetime import datetime
import sys

class NubbinBattery(Battery):


    def __init__(self, current_date: date, last_service_date: date):
        self._current_date = current_date
        self._last_service_date = last_service_date

    def needs_service(self) -> bool:

        service_threshold = 365 * 4   
        time_since_last_service = self._current_date - self._last_service_date   
        return time_since_last_service.days > service_threshold