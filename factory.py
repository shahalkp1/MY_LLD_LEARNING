from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_msg(self, msg):
        pass


class EmailNotif(Notification):
    def send_msg(self, msg):
        print('succussfully send msg: '+ msg)

class whatsappNotif(Notification):
    def send_msg(self, msg):
        print('succussfully send msg: '+ msg)


class NotificationFactory:
    _creators = {
        'EMAIL': EmailNotif,
        'WHATSAPP': whatsappNotif
    }

    @staticmethod
    def create_notif(notification_type):
        target = NotificationFactory._creators.get(notification_type.upper())
        if not target:
            print('e')
        
        return target()

class NotificationService:
    def send_notif(self, notification_type, msg):
        notif = NotificationFactory.create_notif(notification_type)
        notif.send_msg(msg)


if __name__ == '__main__':
    notif = NotificationService()
    notif.send_notif('email', 'heloooooo dear')
