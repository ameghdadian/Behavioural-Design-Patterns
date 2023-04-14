from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Observable
class Subject:
    def __init__(self):
        self.observers:List[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for obs in self.observers:
            obs.update()


# Source of the data
class DataSource(Subject):
    def __init__(self):
        super().__init__()
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.notify_observers()


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class SpreadSheet(Observer):
    def __init__(self, datasource:DataSource):
        self.datasource = datasource

    def update(self):
        # Pull-style of communication
        # Observer is responsible to get the data
        # it needs from Observable. So it has a 
        # reference to it in the constructor.
        print("Spreadsheet got updated: ", self.datasource.value)


class Chart(Observer):
    def __init__(self, datasource: DataSource):
        self.datasource = datasource

    def update(self):
        print("Chart got updated: ", self.datasource.value)

