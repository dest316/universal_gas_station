from models.pump import Pump
from models.fuel_storage import FuelStorage


class RefuelingStation:
    def __init__(self, location: str):
        self.location = location
        self.pumps = []
        self.storages = []
    
    def add_pump(self, pump: Pump):
        self.pumps.append(pump)
    
    def list_pumps(self):
        return [pump.storage.fuel.get_info() for pump in self.pumps]