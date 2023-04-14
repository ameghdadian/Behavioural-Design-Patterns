from __future__ import annotations
from abc import ABC


class UIControl(ABC):
    def __init__(self):
        self.event_handlers = []
    
    def add_event_handler(self, cbk: function):
        self.event_handlers.append(cbk)

    def _notify_event_handlers(self, *args, **kwargs):
        for handler in self.event_handlers:
            handler(*args)

class Button(UIControl):
    def __init__(self):
        super().__init__()
        self._is_enabled = False

    @property
    def is_enabled(self):
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value: bool):
        self._is_enabled = value
        self._notify_event_handlers(value)


class CheckBox(UIControl):
    def __init__(self):
        super().__init__()
        self._is_checked = False

    @property
    def is_checked(self):
        return self._is_checked

    @is_checked.setter
    def is_checked(self, value: bool):
        self._is_checked = value
        self._notify_event_handlers(value)


class TextBox(UIControl):
    def __init__(self):
        super().__init__()
        self._content = False

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self._notify_event_handlers(value)


class SignUpDialogBox:
    def __init__(self):
        self.username = TextBox()
        self.username.add_event_handler(self.changed)
        self.password = TextBox()
        self.password.add_event_handler(self.changed)
        self.agreed_terms = CheckBox()
        self.agreed_terms.add_event_handler(self.changed)
        self.signup_btn = Button()
    
    def simulate_user_interaction(self):
        self.username.content = "Jack"
        self.password.content = "Emptiness"
        self.agreed_terms.is_checked = True

        self.username.content = ""


    def changed(self, value):
        print("new received value", value)
        if (self.username.content and self.password.content
            and self.agreed_terms.is_checked):
            print('Button is now activated!')
            self.signup_btn.is_enabled = True
        else:
            print('Button is not activated!')
            self.signup_btn.is_enabled = False
    

def main():
    dialogbox = SignUpDialogBox()
    dialogbox.simulate_user_interaction()

if __name__ == '__main__':
    main()