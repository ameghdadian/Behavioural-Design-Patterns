from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


"""
    Since after some time, DialogBox's state may
    get bulky, we can use Observer pattern to solve
    this. DialogBox becomes observer and other ui
    controls play the role of observables.
"""


# Observable
class UIControl:
    def __init__(self):
        self.observers = []
    
    def add_observer(self, callback: function):
        self.observers.append(callback)
    
    def _notify_observers(self):
        for obs in self.observers:
            obs()
    

# class Observer(ABC):
#     @abstractmethod
#     def update(self):
#         pass


class ListBox(UIControl):
    def __init__(self):
        super().__init__()
        self._selection = ""

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, value):
        self._selection = value
        self._notify_observers()

    
class TextBox(UIControl):
    def __init__(self):
        super().__init__()
        self._content = ""
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        self._content = value
        self._notify_observers()


class Button(UIControl):
    def __init__(self):
        super().__init__()
        self._is_enabled = False
    
    @property
    def is_enabled(self):
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value):
        self._is_enabled = value
        self._notify_observers()
        

class ArticlesDialogBox:
    def __init__(self):
        self.articles_list_box = ListBox()
        self.articles_list_box.add_observer(self.article_selected)
        self.title_text_box = TextBox()
        self.title_text_box.add_observer(self.title_changed)
        self.save_button = Button()

    def simulate_user_interaction(self):
        self.articles_list_box.selection = "Article 1"
        self.title_text_box.content = ""
        self.title_text_box.content = "Article 2"
        print("TextBox: ", self.title_text_box.content)
        print("Button: ", self.save_button.is_enabled)
    
    def article_selected(self):
        self.title_text_box.content = self.articles_list_box.selection
        self.save_button.is_enabled = True
    
    def title_changed(self):
        content = self.title_text_box.content
        is_empty = not content
        self.save_button.is_enabled = not is_empty