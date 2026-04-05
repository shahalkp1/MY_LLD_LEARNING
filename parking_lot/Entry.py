import uuid
from typing import Optional
from vehicle import *
from parking_lot import *
from parking_lot_ticket import *

class EntryGate:
    def __init__(self, parking_lot: 'ParkingLot'):
        self._parking_lot = parking_lot

    def entry(self, vehicle: 'Vehicle') -> Optional['ParkingLotTicket']:
        return self.issue_ticket(vehicle)

    def issue_ticket(self, vehicle: 'Vehicle') -> Optional['ParkingLotTicket']:

        available_spot = self._parking_lot.find_available_spot(vehicle.get_vehicle_type())

        if available_spot:
            ticket_id = uuid.uuid4()
            ticket = ParkingLotTicket(
                ticket_id=ticket_id, 
                vehicle=vehicle, 
                parking_spot=available_spot
            )
            self._parking_lot.issue_ticket(ticket_id, ticket)
            available_spot.occupy_spot(vehicle)
            print(f"Ticket issued for vehicle: {vehicle.get_license_number()}")
            return ticket
        print(f"No available parking spot for vehicle: {vehicle.get_license_number()}")
        return None