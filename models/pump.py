from typing import Union

from models.fuel_storage import FuelStorage
from models.adapter import Adapter
from models.device import Device


class Pump:
    def __init__(self, storage: FuelStorage):
        self.storage = storage  # Ссылается на хранилище топлива
    
    def pump_fuel(self, amount: float):
        return self.storage.dispense_fuel(amount)
    
    def connect(self, target: Union[Device, Adapter]):
        print("Подключение колонки к устройству.")