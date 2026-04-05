import math
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def calculate(self, duration_ms: int) -> float:
        pass

class HourlyPaymentStrategy(PaymentStrategy):
    HOURLY_RATE = 2.0  
    MS_IN_HOUR = 1000 * 60 * 60

    def calculate(self, duration_ms: int) -> float:
        hours = math.ceil(duration_ms / self.MS_IN_HOUR)
        return float(self.HOURLY_RATE * hours)

class MinutePaymentStrategy(PaymentStrategy):
    MINUTE_RATE = 0.05
    MS_IN_MINUTE = 1000 * 60

    def calculate(self, duration_ms: int) -> float:
        minutes = duration_ms // self.MS_IN_MINUTE  
        return float(self.MINUTE_RATE * minutes)

class PaymentProcessor:
    def __init__(self, strategy: Optional['PaymentStrategy'] = None):
        self._payment_strategy = strategy

    def set_strategy(self, strategy: 'PaymentStrategy'):
        self._payment_strategy = strategy

    def calculate_strategy(self, duration_ms: int) -> float:
        """
        Executes the current strategy's calculation logic.
        """
        if not self._payment_strategy:
            raise ValueError("Payment strategy has not been set.")
            
        return self._payment_strategy.calculate(duration_ms)