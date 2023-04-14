from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class VideoEditor:
    def __init__(self, contrast: float, text:str):
        self._contrast = contrast
        self._text = text
    
    @property
    def contrast(self) -> str:
        return self._contrast

    @contrast.setter
    def contrast(self, contrast):
        self._contrast = contrast

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    def __str__(self) -> str:
        return f"VideoEditor<contrast={self.contrast}, " \
            f"text={self.text}>"


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
    
    def size(self) -> int:
        return len(self.commands)


class ContrastCommand(UndoableCommand):
    def __init__(self, editor: VideoEditor, history: History):
        self.prev_contrast = 0
        self.new_contrast = None
        self.editor = editor
        self.history = history
    
    def set_contrast(self, contrast) -> ContrastCommand:
        self.new_contrast = contrast
        return self
    
    def execute(self):
        self.prev_contrast = self.editor.contrast
        self.editor.contrast = self.new_contrast
        self.history.push(self)
    
    def unexecute(self):
        self.editor.contrast = self.prev_contrast

class TextCommand(UndoableCommand):
    def __init__(self, editor: VideoEditor, history: History):
        self.prev_text = 0
        self.new_text = None
        self.editor = editor
        self.history = history
    
    def set_text(self, text) -> TextCommand:
        self.new_text = text
        return self
    
    def execute(self):
        self.prev_text = self.editor.text
        self.editor.text = self.new_text
        self.history.push(self)
    
    def unexecute(self):
        self.editor.text = self.prev_text
    

class UndoCommand(Command):
    def __init__(self, history: History):
        self.history = history

    def execute(self):
        if self.history.size() > 0:
            self.history.pop().unexecute()


class CompositeCommand:
    def __init__(self):
        self.commands: List[Command] = []

    def add(self, command: Command):
        self.commands.append(command)
    
    def execute(self):
        for command in self.commands:
            command.execute()


def main():
    history = History()
    editor = VideoEditor(10, "V1.vlc")
    composite = CompositeCommand()
    composite.add(ContrastCommand(editor, history).set_contrast(20))
    composite.add(ContrastCommand(editor, history).set_contrast(5))
    composite.add(TextCommand(editor, history).set_text("NewV.vlc"))
    composite.add(ContrastCommand(editor, history).set_contrast(30))
    composite.add(UndoCommand(history))
    # composite.add(UndoCommand(history))
    # composite.add(UndoCommand(history))
    # composite.add(UndoCommand(history))
    # composite.add(UndoCommand(history))
    composite.execute()
    print(editor)


if __name__ == '__main__':
    main()