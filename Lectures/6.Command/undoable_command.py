from abc import ABC, abstractmethod
from typing import List


class HtmlDocument:
    def __init__(self, content):
        self.content = content

    def make_bold(self):
        self.content = f"<b>{self.content}</b>"


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class UndoableCommand(Command):
    @abstractmethod
    def unexecute(self):
        pass


class History:
    def __init__(self):
        self.commands: List[UndoableCommand] = []
    
    def push(self, command: UndoableCommand):
        self.commands.append(command)
    
    def pop(self) -> UndoableCommand:
        last_idx = self.size() - 1
        last_el = self.commands.pop(last_idx)
        return last_el
    
    def size(self):
        return len(self.commands)


class BoldCommand(UndoableCommand):
    def __init__(self, document: HtmlDocument, history: History):
        self.prev_content = ""
        self.document = document
        self.history = history
    
    def execute(self):
        self.prev_content = self.document.content
        self.document.make_bold()
        self.history.push(self)
    
    def unexecute(self):
        self.document.content = self.prev_content


class UndoCommand(Command):
    def __init__(self, history: History):
        self.history = history

    def execute(self):
        if self.history.size() > 0:
            self.history.pop().unexecute()


def main():
    history = History()
    document = HtmlDocument("Hello World")

    bold_command = BoldCommand(document, history)
    bold_command.execute()
    print(document.content)

    # We need an undo command instead of directly undoing this
    # bold_command.unexecute()
    # print(document.content)

    undo_command = UndoCommand(history)
    undo_command.execute()
    print(document.content)



if __name__ == "__main__":
    main()
        