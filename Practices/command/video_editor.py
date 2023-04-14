from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class VideoEditor:
    def __init__(self, label=""):
        self._label = label
        self._contrast = 0.5

    def set_label(self, label):
        self._label = label

    def set_contrast(self, contrast):
        self._contrast = contrast
    
    @property
    def label(self):
        return self._label

    @property
    def contrast(self):
        return self._contrast

    def __str__(self) -> str:
        return f"VideoEditor" \
                f"contrast= {self.contrast}" \
                f", text=' {self.label}"

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class UndoableCommand(Command):
    @abstractmethod
    def unexecute(self):
        pass


class History:
    '''
        Those commands which are not Undoable, is not necessary to keep
        track of, since they cant be undone!
    '''
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


class LabelCommand(UndoableCommand):
    def __init__(self, editor: VideoEditor, history: History):
        self.prev_label = ""
        self.new_label = None
        self.editor = editor
        self.history = history
    
    def set_label(self, label):
        self.new_label = label
        return self

    def execute(self):
        self.prev_label = self.editor.label
        self.editor.set_label(self.new_label)
        self.history.push(self)

    def unexecute(self):
        self.editor.set_label(self.prev_label)


class ContrastCommand(UndoableCommand):
    def __init__(self, editor: VideoEditor, histroy: History):
        self.prev_contrast = 0
        self.new_contrast = None
        self.editor = editor
        self.history = histroy
    
    def set_contrast(self, contrast):
        self.new_contrast = contrast
        return self

    def execute(self):
        self.prev_contrast = self.editor.contrast
        self.editor.set_contrast(self.new_contrast)
        self.history.push(self)

    def unexecute(self):
        self.editor.set_contrast(self.prev_contrast)


class UndoCommand(Command):
    def __init__(self, history: History):
        self.history = history

    def execute(self):
        if self.history.size() > 0:
            self.history.pop().unexecute()


class CompositeCommand(Command):
    def __init__(self):
        self.commands:List[Command] = []

    def add(self, command: Command):
        self.commands.append(command)
    
    def execute(self):
        for command in self.commands:
            command.execute()


def main():
    editor = VideoEditor("Video1.vlc")
    history = History()
    composite = CompositeCommand()
    composite.add(LabelCommand(editor, history).set_label("NewlyUploaded.vlc"))
    composite.add(ContrastCommand(editor, history).set_contrast(20))
    composite.add(LabelCommand(editor, history).set_label("Changer.vlc"))
    composite.add(ContrastCommand(editor, history).set_contrast(30))
    # composite.add(UndoCommand(history))
    # composite.add(UndoCommand(history))
    # composite.add(UndoCommand(history))
    composite.add(UndoCommand(history))
    composite.execute()
    print(editor)



if __name__ == '__main__':
    main()