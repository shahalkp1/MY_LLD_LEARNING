from abc import ABC, abstractmethod

class PaymentStrategy:
    @abstractmethod
    def pay(self):
        pass

class UPIPayment(PaymentStrategy):
    def pay(self):
        print('paid using UPI')

class CardPayment(PaymentStrategy):
    def pay(self):
        print('paid using card')

class payPalPayment(PaymentStrategy):
    def pay(self):
        print('paid using Paypal')

class PaymentService:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def make_payment(self):
        self._strategy.pay()


if __name__ == '__main__':
    service = PaymentService(payPalPayment)
    service.make_payment()
