import vehicle
from enum import Enum

class SpotType(Enum):
    CAR = "CAR"
    TRUCK = "TRUCK"
    BIKE = "BIKE"

    def __init__(self, vehicle_type):
        self.comp_veh_type = vehicle_type

    def can_fit_veh(self, vehicle_type: VehicleType):
        return self.comp_veh_type == vehicle_type


class ParkingSpot:
    def __init__(self, Spot_type:SpotType, spot_id: int):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occuppied = False
        self.parked_vehicle = None

    def occupy_spot(self, vehicle: vehicle):
        self._parked_vehicle = vehicle
        self.is_occuppied = True

    def vacate_spot(self):
        self._parked_vehicle = vehicle
        self.is_occuppied = True

    def check_occuppied(self):
        return self.is_occuppied == True

    def get_spot_type(self):
        return self.spot_type       

