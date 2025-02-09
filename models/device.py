from abc import abstractmethod
from models.refueling_station import RefuelingStation
from patterns.pump_state import PumpStateFree, PumpStateOccupied


class Device:
    def __init__(self, name: str, required_fuel_type: str, gas_tank_capacity: int, gas_tank_port: str, gas_tank_current_volume: int):
        self.name = name
        self.required_fuel_type = required_fuel_type  # Какой тип топлива требует устройство
        self.gas_tank_capacity=gas_tank_capacity
        self.gas_tank_current_volume = gas_tank_current_volume
    
    def refuel(self, gas_station: RefuelingStation, amount: float):
        
        # TODO: Переписать логику: метод должен обращаться к объекту refueling_station, он выступает посредником к колонке.
        # Через этот метод будет получаться доступ к желаемой колонке (ее тоже можно передать в параметрах) через метод 
        # колонки connect()
        if amount > self.gas_tank_capacity - self.gas_tank_current_volume:
            raise ValueError("Попытка заправить слишком большое кол-во топлива")
        self._prepare_to_refuel()
        targer_pump = gas_station.get_free_pump(self.required_fuel_type, amount)
        if not targer_pump:
            print("На данной заправке нет свободных колонок")
        else:
            targer_pump.change_state(PumpStateOccupied())
            self._connect(amount, targer_pump.charge_speed)
            targer_pump.change_state(PumpStateFree())
            targer_pump.fuel_supplies -= amount

    
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