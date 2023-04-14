from abc import ABC, abstractmethod
# Very useful pattern

'''
class Button:
    def __init__(self, label):
        self.label = label 

    def click(self):
        # At the time of designing this class, we dont know
        # what to do when button is clicked, e.g. send an http
        # request, connect to a database
        # Command design pattern comes to the rescue
        pass

    @property
    def label(self):
        return self.label

    @label.setter
    def label(self, value):
        self.label = value
'''


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Button:
    def __init__(self, command: Command):
        self._label = ""
        self.command = command

    def click(self):
        self.command.execute()

    @property
    def label(self):
        return self.label

    @label.setter
    def label(self, value):
        self.label = value
    

# 
# Now, building an application using above framework
# 
class CustomerService:
    def add_customer(self):
        print("Add customer")


class AddCustomerCommand(Command):
    def __init__(self, service: CustomerService):
        self.service = service

    def execute(self):
        self.service.add_customer()
