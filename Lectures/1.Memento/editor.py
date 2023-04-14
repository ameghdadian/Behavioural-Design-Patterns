from __future__ import annotations
# Implementing Undo mechanism

class Editor:
    def __init__(self):
        self._content = ""

    def create_state(self) -> EditorState:
        return EditorState(self.content)
    
    def restore(self, state: EditorState):
        self.content = state.content
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        self._content = value


class EditorState:
    def __init__(self, content: str):
        self._content = content

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        self._content = value
    

class History:
    def __init__(self):
        self.states: list[EditorState] = []

    def push(self, state: EditorState):
       self.states.append(state) 
    
    def pop(self) -> EditorState:
        last_indx = len(self.states) - 1
        return self.states.pop(last_indx)
