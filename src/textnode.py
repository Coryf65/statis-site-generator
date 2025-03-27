from enum import Enum

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"
    
class TextNode:
    def __init__(self, text = None, text_type = None, url = None):
        # The text content of the node
        self.text = text
        # The type of text this node contains, which is a member of the TextType enum.
        self.text_type = text_type
        # The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
        self.url = url
        
    def __eq__(self, other_text_node):
        is_equal = True
        if self.text != other_text_node.text:
            is_equal = False
        if self.text_type != other_text_node.text_type:
            is_equal = False
        if self.url != other_text_node.url:
            is_equal = False
        return is_equal
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
