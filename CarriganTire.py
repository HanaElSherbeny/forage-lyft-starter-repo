import Tire

class CarriganTire(Tire):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array
    
    def needs_service(self):
        return any(wear >= 0.9 for wear in self.sensor_array)
    