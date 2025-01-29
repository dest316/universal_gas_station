from models.pump import Pump


class Device:
    def __init__(self, name: str, required_fuel_type: str):
        self.name = name
        self.required_fuel_type = required_fuel_type  # Какой тип топлива требует устройство
    
    def refuel(self, pump: Pump, amount: float):
        if pump.storage.fuel.fuel_type != self.required_fuel_type:
            return "Несовместимый тип топлива!"
        return pump.pump_fuel(amount)
