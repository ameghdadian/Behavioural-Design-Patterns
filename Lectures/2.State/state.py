# Behave differently based on the current state
from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def mouse_down(self):
        pass

    @abstractmethod
    def mouse_up(self):
        pass

class SelectionTool(Tool):
    def mouse_down(self):
        print("Selection icon")

    def mouse_up(self):
        print("Draw a dashed rectangle")


class BrushTool(Tool):
    def mouse_down(self):
        print("Brush icon")

    def mouse_up(self):
        print("Draw a line")


class Canvas:
    def __init__(self):
        self._current_tool: Tool = None

    def mouse_down(self):
        self.current_tool.mouse_down()

    def mouse_up(self):
        self.current_tool.mouse_up()

    @property
    def current_tool(self) -> Tool:
        return self._current_tool
    @current_tool.setter
    def current_tool(self, tool: Tool):
        self._current_tool = tool