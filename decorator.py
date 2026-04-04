from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, msg):
        pass

class BaseNotifier(Notifier):
    def send(self, message):
        print('Triggered')

class NotifierDecorator(Notifier):
    def __init__(self, notifier:Notifier):
        self._notifier = notifier
    
    def send(self, msg):
        self._notifier.send(msg)

class SMSNotifier(NotifierDecorator):
    def send(self, msg):
        super().send(msg)
        print('SMS Send')

class WhatsappNotifier(NotifierDecorator):
    def send(self, msg):
        super().send(msg)
        print('whatsapp send')

if __name__ == '__main__':
    notifier = WhatsappNotifier(SMSNotifier(BaseNotifier()))
    notifier.send('Sending..')
        
