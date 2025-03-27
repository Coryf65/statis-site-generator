#!/usr/bin/python3


class HTMLNode:
    """
    class HTMLNode
    
    A class to represent an HTML Node    
    
    :param tag: A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    :param value: A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    :param children: A list of HTMLNode objects representing the children of this node
    :param props: A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
        
    def __repr__(self):
        return f"HTMLNode: tag '{self.tag}' value '{self.value}' children '{self.children}' props '{self.props}'"