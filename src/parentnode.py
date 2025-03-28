#!/usr/bin/python3

from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    """
    
    """
    
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode(<tag>): Cannot turn to HTML without an HTML tag")
        
        return super().to_html()