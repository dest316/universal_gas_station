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
    
    
    def get_free_pump(self, fueled_device: Device, required_amount: float) -> Pump|None:
        suitable_pumps = list(filter(
            lambda x: x.get_readiness(required_amount) and fueled_device.required_fuel_type == x.fuel_type, self.pumps
        ))
        # Если свободных колонок несколько - возвращаем с самым большим запасом топлива
        if suitable_pumps:
            return sorted(suitable_pumps, key=lambda x: x.fuel_supplies)[-1]
        return None
        # Какая-то логика подбора свободной колонки из списка существующих на заправке
        # Сначала ищем свободные колонки по типу топлива, потом среди них - удовлетворяющие
        # экстра потребностям девайса (для электрических это может быть минимальная сила тока,
        # для бензиновых - рэндж допустимых октановых чисел) и должно быть топлива >= требуется заправить
        # в устройство