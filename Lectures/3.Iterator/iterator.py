from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


# Pythonic/Idiomatic way
class BrowseHistory:
    # ??????????????????????
    # One thing to note: Here, we are good to go
    # if we decide to change the data structure 
    # for storing elements. We need to change the
    # __iter__ function return type (and some other
    # stuff, which the scope of changes are only limited to
    # this class, and not the clients!).
    # ??????????????????????
    def __init__(self):
        self._urls: List[str] = []

    def push(self, url: str):
        self._urls.append(url)
    
    def pop(self) -> str:
        last_idx = len(self._urls) - 1
        return self._urls.pop(last_idx)

    def __iter__(self):
        return BrowseHistoryIterator(self._urls)
    

class BrowseHistoryIterator:
    def __init__(self, urls: List[str]):
        self.urls = urls
        self.idx = 0

    def __next__(self):
        if self.idx > len(self.urls) - 1:
            raise StopIteration

        element = self.urls[self.idx]
        self.idx += 1
        return element


# Generic implementation
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass


class GenericBrowseHistory:
    # ??????????????????????
    # One thing to note: Here, we are good to go
    # if we decide to change the data structure 
    # for storing elements. We need to change the
    # __iter__ function return type.
    # ??????????????????????
    def __init__(self):
        self._urls: List[str] = []

    def push(self, url: str):
        self._urls.append(url)
    
    def pop(self) -> str:
        last_idx = len(self._urls) - 1
        return self._urls.pop(last_idx)
    
    def create_iterator(self) -> Iterator:
        return self.ListIterator(self)

    class ListIterator(Iterator):
        def __init__(self, history: BrowseHistory):
            self.history = history
            self.indx = 0
        
        def has_next(self) -> bool:
            has_more = self.indx < len(self.history._urls)
            if not has_more:
                raise StopIteration

            return has_more

        def current(self):
            if self.has_next():
                element = self.history._urls[self.indx]
                self.next()
                return element
        
        def next(self):
            self.indx += 1

        # These two methods implemented for the sake of conforming
        # with Python specifications :)
        def __iter__(self):
            return self
        def __next__(self):
            return self.current()
