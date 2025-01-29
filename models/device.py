from abc import abstractmethod
from models.pump import Pump


class Device:
    def __init__(self, name: str, required_fuel_type: str, gas_tank_capacity: int, gas_tank_port: str):
        self.name = name
        self.required_fuel_type = required_fuel_type  # Какой тип топлива требует устройство
        self.gas_tank_capacity=gas_tank_capacity
    
    def refuel(self, pump: Pump, amount: float):
        
        # TODO: Переписать логику: метод должен обращаться к объекту refueling_station, он выступает посредником к колонке.
        # Через этот метод будет получаться доступ к желаемой колонке (ее тоже можно передать в параметрах) через метод 
        # колонки connect()
        if pump.storage.fuel.fuel_type != self.required_fuel_type:
            return "Несовместимый тип топлива!"
        return pump.pump_fuel(amount)
    
    @abstractmethod
    def _prepare_to_refuel():
        print("Какая-то логика действий для подготовки к заправке")

