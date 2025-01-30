from models.pump import Pump
from models.device import Device
from models.fuel_storage import FuelStorage


class RefuelingStation:
    def __init__(self, location: str):
        self.location = location
        self.pumps = []
        self.storages = []
    
    def add_pump(self, pump: Pump):
        self.pumps.append(pump)
    
    def list_pumps(self):
        return [pump.storage.fuel.get_info() for pump in self.pumps]
    
    def get_free_pump(self, fueled_device: Device, required_amount: float) -> Pump|None:
        # Какая-то логика подбора свободной колонки из списка существующих на заправке
        # Сначала ищем свободные колонки по типу топлива, потом среди них - удовлетворяющие
        # экстра потребностям девайса (для электрических это может быть минимальная сила тока,
        # для бензиновых - рэндж допустимых октановых чисел) и должно быть топлива >= требуется заправить
        # в устройство
        pass