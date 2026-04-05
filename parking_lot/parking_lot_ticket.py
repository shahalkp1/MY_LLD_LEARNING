import time
from uuid import UUID
from dataclasses import dataclass, field
from vehicle import *
from parking_spot import *

@dataclass(frozen=True)
class ParkingLotTicket:

    ticket_id: UUID
    vehicle: 'Vehicle'
    parking_spot: 'ParkingSpot'
    entry_time: float = field(default_factory=lambda: time.time() * 1000)