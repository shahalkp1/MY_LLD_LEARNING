from abc import ABC, abstractmethod

class Observer:
    @abstractmethod
    def update(self):
        pass

class Subject:
    @abstractmethod
    def attach(self, Observer:Observer):
        pass

    @abstractmethod
    def detach(self, Observer:Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class NewsAgency:
    def __init__(self):
        self._observer = []
        self._news = ''

    def attach(self, observer:Observer):
        if observer not in self._observer:
            self._observer.append(observer)

    def detach(self, observer:Observer):
        if observer in self._observer:
            self._observer.remove(observer)

    def notify(self):
        for observer in self._observer:
            observer.update(self._news)

    def set_news(self, news):
        self._news = news
        self.notify()

class NewsChannel:
    def __init__(self, ChannelName):
        self.ChannelName = ChannelName

    def update(self, news):
        print(self.ChannelName + ' rcvd '+ news)


if __name__ == '__main__':
    agency = NewsAgency()

    cnn = NewsChannel('cnn')
    bbc = NewsChannel('bbc')

    agency.attach(cnn)
    agency.attach(bbc)

    agency.set_news('this is news')
