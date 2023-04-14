from __future__ import annotations
from typing import List

class Document:
    def __init__(self):
        self._content = ""
        self._font_name = ""
        self._font_size = -1

    def create_state(self):
        return DocumentMemento(
            self.content,
            self.font_size,
            self.font_name
        )

    def restore(self, state: DocumentMemento):
        self.content = state._content
        self.font_size = state._font_size
        self.font_name = state._font_name

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, value):
        self._font_name = value

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = value

    def __str__(self) -> str:
        return f'Content: {self.content}, '\
            f'Font Name: {self.font_name}, Font Size: {self.font_size}'

class DocumentMemento:
    def __init__(self, content, font_size, font_name):
        self._content = content
        self._font_size = font_size
        self._font_name = font_name


class History:
    def __init__(self):
        self.states: List[DocumentMemento] = []

    def push(self, state: DocumentMemento):
        self.states.append(state)

    def pop(self):
        last_idx = len(self.states) - 1
        return self.states.pop(last_idx)

