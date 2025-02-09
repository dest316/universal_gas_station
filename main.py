"""Точка входа в приложение"""

from models.refueling_station import RefuelingStation
from models.pump import Pump
from models.fuel import Fuel
from models.fuel_storage import FuelStorage
from patterns.device_factory import DeviceFactory

# Создаем заправку
station = RefuelingStation("main_station")

# Создаем вид топлива
gasoline = Fuel("gasoline", 1)

# Создаем хранилище топлива
storage = FuelStorage(gasoline, 1000)

# Создаем колонку
pump = Pump(storage, 1)

# Добавляем новую колонку к заправке
station.add_pump(pump)

# Создаем экземпляр автомобиля с помощью фабрики
my_car = DeviceFactory.create_device("Car", gas_tank_capacity=70, gas_tank_current_volume=0)
your_car = DeviceFactory.create_device("Car", gas_tank_capacity=2000, gas_tank_current_volume=0)

my_car.refuel(station, 60)
your_car.refuel(station, 100)
