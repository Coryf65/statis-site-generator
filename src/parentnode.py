#!/usr/bin/python3

from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    """
    class LeafNode
    
    A class to represent an Leaf Node a node with no children
    
    :param tag: A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    :param value: A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    :param children: A list of HTMLNode objects representing the children of this node
    :param props: A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """
    
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode(<tag>): Cannot turn to HTML without an HTML tag")
        if self.children is None:
            raise ValueError("ParentNode(<children>): Cannot turn to HTML without children tag")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"