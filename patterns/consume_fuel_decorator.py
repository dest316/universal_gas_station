from functools import wraps

def set_limit(func):
    """Декоратор, ограничивающий максимальный объем топлива."""
    @wraps(func)
    def wrapper(self, fuel_batch_size: float, fuel_total_size: float):
        limit = self.gas_tank_capacity  # Динамически берем лимит из объекта
        if fuel_total_size > limit:
            print(f"⚠ Ограничение: Заправка ограничена {limit} литрами вместо {fuel_total_size}.")
            fuel_total_size = limit
        return func(self, fuel_batch_size, fuel_total_size)
    return wrapper