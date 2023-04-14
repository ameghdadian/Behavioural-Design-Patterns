from __future__ import annotations
from abc import ABC, abstractmethod


# Mediator
class DialogBox(ABC):
    @abstractmethod
    def changed(self, control:UIControl):
        pass


class UIControl:
    # Every UIControl needs to know its mediator
    def __init__(self, owner: DialogBox):
        self.owner = owner


class ListBox(UIControl):
    def __init__(self, owner: DialogBox):
        super().__init__(owner)
        self._selection = ""

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, value):
        self._selection = value
        self.owner.changed(self)

    
class TextBox(UIControl):
    def __init__(self, owner: DialogBox):
        super().__init__(owner)
        self._content = ""
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        self._content = value
        self.owner.changed(self)


class Button(UIControl):
    def __init__(self, owner: DialogBox):
        super().__init__(owner)
        self._is_enabled = False
    
    @property
    def is_enabled(self):
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value):
        self._is_enabled = value
        self.owner.changed(self)
        

class ArticlesDialogBox(DialogBox):
    def __init__(self):
        self.articles_list_box = ListBox(self)
        self.title_text_box = TextBox(self)
        self.save_button = Button(self)

    def simulate_user_interaction(self):
        self.articles_list_box.selection = "Article 1"
        self.title_text_box.content = ""
        self.title_text_box.content = "Article 2"
        print("TextBox: ", self.title_text_box.content)
        print("Button: ", self.save_button.is_enabled)

    def changed(self, control: UIControl):
        if isinstance(control, ListBox):
            self.article_selected()
        elif isinstance(control, TextBox):
            self.title_changed()

    def article_selected(self):
        self.title_text_box.content = self.articles_list_box.selection
        self.save_button.is_enabled = True
    
    def title_changed(self):
        content = self.title_text_box.content
        is_empty = not content
        self.save_button.is_enabled = not is_empty