import time
from uuid import UUID
from parking_lot import *
from parking_lot_ticket import *

class ExitGate:
    def __init__(self, parking_lot: 'ParkingLot'):
        self._parking_lot = parking_lot

    def exit(self, ticket_id: UUID):
        ticket = self._parking_lot.get_ticket_by_id(ticket_id)
        if ticket:
            exit_time = time.time() * 1000
            duration = exit_time - ticket.get_entry_time()
            processor = self._parking_lot.get_payment_processor()
            fee = processor.calculate_strategy(duration)
            license_plate = ticket.get_vehicle().get_license_number()
            print(f"Vehicle {license_plate} exited. Parking fee: ${fee:.2f}")
            ticket.get_parking_spot().vacate_spot()
            self._parking_lot.remove_ticket(ticket_id)
            
        else:
            print(f"Invalid ticket ID: {ticket_id}")