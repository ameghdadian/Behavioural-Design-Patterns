from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


'''
    Visitor allows us to add new operation to an
    object structure without altering any existing
    code(object tree).
'''
class Operation(ABC):
    @abstractmethod
    def apply_heading_node(self, heading: HeadingNode):
        pass

    @abstractmethod
    def apply_anchor_node(self, anchor: AnchorNode):
        pass


class HighlightOperation(Operation):
    def apply_heading_node(self, heading: HeadingNode):
        print("Highlight anchor")

    def apply_anchor_node(self, anchor: AnchorNode):
        print("Highlight heading")


class PlainTextOperation(Operation):
    def apply_heading_node(self, heading: HeadingNode):
        print("text heading")

    def apply_anchor_node(self, anchor: AnchorNode):
        print("text anchor")


class HtmlNode(ABC):
    @abstractmethod
    def execute(self, operation: Operation):
        pass


class HeadingNode(HtmlNode):
    def execute(self, operation: Operation):
        operation.apply_heading_node(self)


class AnchorNode(HtmlNode):
    def execute(self, operation: Operation):
        operation.apply_anchor_node(self)


class HtmlDocument:
    def __init__(self):
        self.nodes:List[HtmlNode] = []
    
    def add(self, node: HtmlNode):
        self.nodes.append(node)
    
    def execute(self, operation: Operation):
        for node in self.nodes:
            node.execute(operation)


def main():
    document = HtmlDocument()
    document.add(HeadingNode())
    document.add(AnchorNode())
    # document.execute(HighlightOperation())
    document.execute(PlainTextOperation())


if __name__ == '__main__':
    main()
