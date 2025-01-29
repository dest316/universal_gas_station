from models.device import Device
from models.pump import Pump


class Adapter:
    def __init__(self, incompatible_device: Device, compatible_fuel_type: str):
        self.incompatible_device = incompatible_device  # Несовместимое устройство
        self.compatible_fuel_type = compatible_fuel_type  # Новый совместимый тип топлива
    
    def adapt(self, pump: Pump, amount: float):
        if pump.storage.fuel.fuel_type == self.compatible_fuel_type:
            return self.incompatible_device.refuel(pump, amount)
        return "Адаптер не может преобразовать это топливо"
    