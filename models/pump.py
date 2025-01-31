from typing import Union

from models.fuel_storage import FuelStorage
from models.adapter import Adapter
from models.device import Device
from patterns.pump_state import PumpState, PumpStateFree


class Pump:
    # скорость зарядки
    charge_speed: float
    state: PumpState = PumpStateFree()
    fuel_supplies: float
    fuel_type: str

    def __init__(self, storage: FuelStorage):
        self.storage = storage  # Ссылается на хранилище топлива

    def change_state(self, new_state: PumpState):
        self.state = new_state
    
    def pump_fuel(self, amount: float):
        return self.storage.dispense_fuel(amount)
    
    def connect(self, target: Union[Device, Adapter]):
        print("Подключение колонки к устройству.")

    def get_readiness(self, required_amount: float):
        return self.state.get_readiness(required_amount, self.fuel_supplies)