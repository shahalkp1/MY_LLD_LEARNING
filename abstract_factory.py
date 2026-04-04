from abc import ABC, abstractmethod

class SMS(ABC):
    @abstractmethod
    def send(self, msg):
        print(msg)

class EMAIL(ABC):
    @abstractmethod
    def send(self, msg):
        print(msg)

class AWSEmail(EMAIL):
    def send(self, msg):
        print(msg)

class AWSSMS(SMS):
    def send(self, msg):
        print(msg)

class AzureEMAIL(EMAIL):
    def send(self, msg):
        print(msg)

class AzureSMS(SMS):
    def send(self, msg):
        print(msg)


class comm_fact(ABC):
    @abstractmethod
    def create_email(self, msg):
        pass

    @abstractmethod
    def create_sms(self, msg):
        pass

class AWSFact(comm_fact):
    def create_email(self):
        return AWSEmail()

    def create_sms(self):
        return AWSSMS()

class AzureFact(comm_fact):
    def create_email(self):
        return AzureEMAIL()

    def create_sms(self):
        return AzureSMS()

class Notification:
    def __init__(self, factory: comm_fact):
        self.factory = factory

    def alert_admin(self, msg):
        email = self.factory.create_email()
        sms = self.factory.create_sms()

        email.send(msg)
        sms.send(msg)


if __name__ == '__main__':
    aws_service = Notification(AWSFact())
    aws_service.alert_admin('hiiiii') 
