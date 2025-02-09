from models.device import Device
from patterns.consume_fuel_decorator import set_limit


class Car(Device):
    def __init__(self, **kwargs):
        super().__init__(name="Car", required_fuel_type="gasoline", gas_tank_capacity=50, gas_tank_port="gasoline_standart", gas_tank_current_volume=0)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _prepare_to_refuel(self):
        print("Глушим двигатель...")
        print("Открываем крышку бензобака...")
    
    @set_limit
    def _consume_fuel(self, fuel_batch_size, fuel_total_size):
        return super()._consume_fuel(fuel_batch_size, fuel_total_size)


class ElectricScooter(Device):
    def __init__(self, **kwargs):
        super().__init__(name="Electric Scooter", required_fuel_type="electricity", gas_tank_capacity=7000, gas_tank_port="usb-c", gas_tank_current_volume=0)
        for key, value in kwargs:
            setattr(self, key, value)
    def _prepare_to_refuel(self):
        print("Выключаем скутер...")
        print("Убираем заглушку с порта зарядки...")

class Spaceship(Device):
    def __init__(self):
        super().__init__(name="Spaceship", required_fuel_type="augmented_uranus", gas_tank_capacity=2500, gas_tank_port="spaceship_port", gas_tank_current_volume=0)
    def _prepare_to_refuel(self):
        print("Переводим корабль в режим зависания...")
        print("Глушим основные двигатели...")
        print("Открываем створку внутреннего хранилища топлива...")


class DeviceFactory:
    @staticmethod
    def create_device(device_type: str, **kwargs):
        device_type = device_type.capitalize()
        if device_type == "Car":
            return Car(**kwargs)
        elif device_type == "Electric Scooter":
            return ElectricScooter(**kwargs)
        elif device_type == "Spaceship":
            return Spaceship(**kwargs)
        else:
            raise ValueError(f"Неизвестный тип устройства: {device_type}")