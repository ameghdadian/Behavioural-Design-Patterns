from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod

from product import Product


class Iterator(ABC):
  @abstractmethod
  def has_next(self):
    pass

  @abstractmethod
  def next(self):
    pass

  @abstractmethod
  def current(self):
    pass


class ProductCollection:
  def __init__(self):
    self.products: List[Product] = []

  def add(self, product: Product):
    self.products.append(product)
  
  def create_iterator(self) -> Iterator:
    return self.ProductCollectionIterator(self)
  
  class ProductCollectionIterator(Iterator):
    def __init__(self, collection: ProductCollection):
      self.collection = collection
      self.idx = 0

    def has_next(self):
      has_more = self.idx < len(self.collection.products)
      if not has_more:
        raise StopIteration
      
      return has_more

    def next(self):
      self.idx += 1

    def current(self):
      if self.has_next():
        element = self.collection.products[self.idx]
        self.next()
        return element

    def __iter__(self):
      return self
    
    def __next__(self):
      return self.current()
