
class NubbinBattery(Battery):
    """A Nubbin car battery."""

    def __init__(self, current_date: date, last_service_date: date):
        self._current_date = current_date
        self._last_service_date = last_service_date

    def needs_service(self) -> bool:
        # turn years to days
        service_threshold = 365 * 4   
        time_since_last_service = self._current_date - self._last_service_date  # type: datetime.timedelta
        return time_since_last_service.days > service_threshold