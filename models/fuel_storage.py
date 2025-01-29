from models.fuel import Fuel


class FuelStorage:
    def __init__(self, fuel: Fuel, capacity: float):
        self.fuel = fuel
        self.capacity = capacity  # Общий объем хранилища
        self.current_volume = capacity  # Текущее количество топлива
    
    def dispense_fuel(self, amount: float):
        if amount > self.current_volume:
            return "Недостаточно топлива!"
        self.current_volume -= amount
        return f"Выдано {amount} единиц {self.fuel.fuel_type}"
    
    def refill(self, amount: float):
        if self.current_volume + amount > self.capacity:
            return "Хранилище переполнится!"
        self.current_volume += amount
        return f"Добавлено {amount} единиц {self.fuel.fuel_type}"