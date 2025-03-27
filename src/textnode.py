from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"
    
class TextNode:
    """
    class TextNode
    
    A class to represent an Text Node    
    
    :param text: The text content of the node
    :param text_type: The type of text this node contains, which is a member of the TextType enum.
    :param url: The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
    """
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other_text_node):
        return (
            self.text_type == other_text_node.text_type
            and self.text == other_text_node.text
            and self.url == other_text_node.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
