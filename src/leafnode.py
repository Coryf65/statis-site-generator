#!/usr/bin/python3

from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    """
    class LeafNode
    
    A class to represent an Leaf Node a node with no children
    
    :param tag: A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    :param value: A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    :param props: A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """

    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")

        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"