from __future__ import annotations
from abc import ABC, abstractmethod



class DataReader:
    def __init__(self, handler: Handler):
        self.handler = handler
        
    def read(self, file: File):
        if not self.handler.handle(file):
            raise Exception("File format not supported.")
    

class Handler(ABC):
    def __init__(self, next: Handler):
        self.next = next

    def handle(self, file: File):
        if self.do_handle(file):
            print("Request fulfilled!")
            return True
        
        if self.next != None:
            return self.next.handle(file)

    @abstractmethod
    def do_handle(self, file: File):
        pass


class File:
    def __init__(self, name, format):
        self.name = name
        self.format = format


class ExcelHandler(Handler):
    format = "xls"
    def do_handle(self, file: File):
        print(1)
        if file.format == ExcelHandler.format:
            print("Handling an excel file")
            return True


class NumberSheetHandler(Handler):
    format = "numbers"
    def do_handle(self, file: File):
        print(2)
        if file.format == NumberSheetHandler.format:
            print("Handling an number spreadsheet file")
            return True


class QuickBookHandler(Handler):
    format = "qwb"
    def do_handle(self, file: File):
        print(3)
        if file.format == QuickBookHandler.format:
            print('here')
            print("Handling a QuickBook workbook file")
            return True


def main():
    file = File("Exc1", "qwb")
    exc_handler = ExcelHandler(None)
    num_handler = NumberSheetHandler(exc_handler)
    qbk_handler = QuickBookHandler(num_handler)

    reader = DataReader(qbk_handler)
    reader.read(file)


if __name__ == '__main__':
    main()