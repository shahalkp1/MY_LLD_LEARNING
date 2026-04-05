from vehicle import *
from parking_spot import *


class ParkingLevel:
    def __init__(self, level_id: int, spots: List['ParkingSpot']):
        self.level_id = level_id
        self.spots = spots

    def find_parking_spots(self, vehicle_type):

        for spot in self.spots:
            if spot.check_occuppied() and spot.get_spot_type().can_fit_veh(vehicle_type):
                return spot

        return None

    def is_full(self):
        for spot in self.spots:
            if spot.check_occuppied():
                return False

        return True

