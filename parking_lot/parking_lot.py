import threading
from typing import List, Dict, Optional
from uuid import UUID 
from parked_vehicle import *
from vehicle import *


class parking_lot:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        
        return cls._instance

    def __init__(self, strategy=None):
        if not hasattr(self, "_initialized"):
            self.levels: List[ParkingLevel] = []
            self.tickets: Dict[UUID, 'ParkinglotTicket'] = {}
            self._initialized = True

    def add_level(self, level:ParkingLevel):
        self.levels.append(level)

    def find_available_spot(self, v_type: VehicleType):

        for level in self.levels:
            spot = level.find_parking_spots(v_type)
            if spot:
                return spot
        return None

    def issue_ticket(self, ticket_id: UUID, ticket: ParkinglotTicket):
        self.tickets[ticket_id] = ticket

    def get_ticket(self, ticket_id:UUID):
        return self.tickets.get(ticket_id, None)





