class PumpState:
    FREE = "свободна"
    OCCUPIED = "занята"

    @staticmethod
    def get_readiness(required_amount: float, fuel_supplies: float):
        raise NotImplementedError()
    


class PumpStateFree(PumpState):
    @staticmethod
    def get_readiness(required_amount, fuel_supplies):
        return required_amount <= fuel_supplies
    

class PumpStateOccupied(PumpState):
    @staticmethod
    def get_readiness(required_amount, fuel_supplies):
        return False