from models.pump import Pump


class RefuelingStation:
    def __init__(self, location: str):
        self.location = location
        self.pumps:list[Pump] = []
        self.storages = []
    
    def add_pump(self, pump: Pump):
        self.pumps.append(pump)
    
    
    def get_free_pump(self, required_fuel_type: str, required_amount: float) -> Pump|None:
        print(f"required_fuel_type = {required_fuel_type}, pump_fuel_type = {self.pumps[0].fuel_type}")
        suitable_pumps = list(filter(
            lambda x: x.get_readiness(required_amount) and required_fuel_type == x.fuel_type, self.pumps
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