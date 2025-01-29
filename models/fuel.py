class Fuel:
    def __init__(self, fuel_type: str, efficiency: float):
        self.fuel_type = fuel_type  # Тип топлива (бензин, электричество и т. д.)
        self.efficiency = efficiency  # Коэффициент эффективности топлива
    
    def get_info(self):
        return f"Тип топлива: {self.fuel_type}, Эффективность: {self.efficiency}"