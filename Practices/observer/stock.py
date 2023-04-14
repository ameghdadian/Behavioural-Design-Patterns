from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Observable:
    def __init__(self):
        self.observers:List[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, observer: Observer):
        for obs in self.observers:
            obs.update(observer)


class Stock(Observable):
    def __init__(self, symbol: str, price: float):
        super().__init__()
        self._symbol = symbol
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        self.notify_observers(self)
    
    @property
    def symbol(self):
        return self._symbol
    
    def __str__(self):
        return f"Stock<price={self._price}, " \
            f"symbol={self._symbol}"


class Observer(ABC):
    @abstractmethod
    def update(self, observable: Observable):
        pass
    
    def add_stock(self, stock: Stock):
        self.stocks.append(stock)
        stock.add_observer(self)

    def show(self):
        for stock in self.stocks:
            print(stock)
    

class StatusBar(Observer):
    def __init__(self):
        super().__init__()
        self.stocks: List[Stock] = []

    def update(self, stock: Stock):
        print("Refreshing Status Bar:")
        self.show()


class StockListView(Observer):
    def __init__(self):
        super().__init__()
        self.stocks: List[Stock] = []

    def update(self, stock: Stock):
        print("Refreshing Stock List View:")
        self.show()


def main():
    stock1 = Stock("Famli", 10)
    stock2 = Stock("Ardestan", 20)
    stock3 = Stock("Petro", 5)

    statusbar = StatusBar()
    stocklistview = StockListView()

    stocklistview.add_stock(stock1)
    stocklistview.add_stock(stock2)
    stocklistview.add_stock(stock3)
    
    # Status bar shows only popular stocks
    statusbar.add_stock(stock1)
    statusbar.add_stock(stock2)

    stock3.price = 40


if __name__ == '__main__':
    main()
