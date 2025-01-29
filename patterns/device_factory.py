from models.device import Device


class Car(Device):
    def __init__(self, **kwargs):
        super().__init__(name="Car", required_fuel_type="gasoline", gas_tank_capacity=50, gas_tank_port="gasoline_standart")
        for key, value in kwargs:
            setattr(self, key, value)
    def _prepare_to_refuel():
        print("Глушим двигатель...")
        print("Открываем крышку бензобака...")


class ElectricScooter(Device):
    def __init__(self):
        super().__init__(name="Electric Scooter", required_fuel_type="electricity", gas_tank_capacity=7000, gas_tank_port="usb-c")
    def _prepare_to_refuel():
        print("Выключаем скутер...")
        print("Убираем заглушку с порта зарядки...")

class Spaceship(Device):
    def __init__(self):
        super().__init__(name="Spaceship", required_fuel_type="augmented_uranus", gas_tank_capacity=2500, gas_tank_port="spaceship_port")
    def _prepare_to_refuel():
        print("Переводим корабль в режим зависания...")
        print("Глушим основные двигатели...")
        print("Открываем створку внутреннего хранилища топлива...")


class DeviceFactory:
    @staticmethod
    def create_device(device_type: str, **kwargs):
        device_type = device_type.capitalize()
        if device_type == "Car":
            return Car()
        elif device_type == "Electric Scooter":
            return ElectricScooter()
        elif device_type == "Spaceship":
            return Spaceship()
        else:
            raise ValueError(f"Неизвестный тип устройства: {device_type}")