from abc import ABC 
from enum import Enum  

class VehicleType(Enum):
    CAR = "CAR"
    TRUCK = "TRUCK"
    BIKE = "BIKE"

class vehicle(ABC):
    def __init__(self, Number:str, Vtype: VehicleType):
        self.Number = Number
        self.Vtype = Vtype

    def get_Number(self) ->str:
        return self.Number

    def get_Vtype(self) ->VehicleType:
        return self.Vtype

class Truck(vehicle):
    def __init__(self, number):
        super().__init__(number, VehicleType.TRUCK)

class Bike(vehicle):
    def __init__(self, number):
        super().__init__(number, VehicleType.BIKE)

class Car(vehicle):
    def __init__(self, number):
        super().__init__(number, VehicleType.CAR)