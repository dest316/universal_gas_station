from abc import abstractmethod
from models.pump import Pump
from models.refueling_station import RefuelingStation


class Device:
    def __init__(self, name: str, required_fuel_type: str, gas_tank_capacity: int, gas_tank_port: str):
        self.name = name
        self.required_fuel_type = required_fuel_type  # Какой тип топлива требует устройство
        self.gas_tank_capacity=gas_tank_capacity
    
    def refuel(self, gas_station: RefuelingStation, amount: float):
        
        # TODO: Переписать логику: метод должен обращаться к объекту refueling_station, он выступает посредником к колонке.
        # Через этот метод будет получаться доступ к желаемой колонке (ее тоже можно передать в параметрах) через метод 
        # колонки connect()
        self._prepare_to_refuel()
        targer_pump = gas_station.get_free_pump(self, amount)
        if not targer_pump:
            print("На данной заправке нет свободных колонок")
        else:
            self._connect(amount, targer_pump.charge_speed)
    
    @abstractmethod
    def _prepare_to_refuel():
        print("Какая-то логика действий для подготовки к заправке")

    def _connect(self, amount, charge_speed):
        print("Колонка соединена с устройством")
        self._consume_fuel(charge_speed, amount)
        # Позже сюда можно добавить логику подключения адаптера к устройству
    def _consume_fuel(self, fuel_batch_size: float, fuel_total_size: float):
        for i in range(0, fuel_total_size, fuel_batch_size):
            # можно написать словарь, вида {тип топлива: ед. измерения} и подставлять в вывод значение оттуда
            print(f"Заправлено уже {i} {self.required_fuel_type}.")
        print("Заправка окончена")