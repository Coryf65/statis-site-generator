#!/usr/bin/python3

from textnode import TextType

class Utilities:
    
    #we need to be able to create TextNodes from raw markdown strings
    
    # given: This is text with a **bolded phrase** in the middle
    # should be: [ TextNode("This is text with a ", TextType.TEXT), TextNode("bolded phrase", TextType.BOLD), TextNode(" in the middle", TextType.TEXT), ]
    
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        """
        Splits the nodes based on the provided delimiter and returns a list of nodes.
        
        :param old_nodes: The nodes to be split.
        :param delimiter: The delimiter used for splitting the nodes ('`', '**').
        :param text_type: The type of text (e.g., 'text', 'bold', 'link') for processing.
        :return: a new list of nodes, where any "text" type nodes in the input list are (potentially) split into multiple nodes based on the syntax
        """
        if text_type == TextType.TEXT:
            return old_nodes.split(delimiter)
        elif text_type == TextType.LINK:
            pass
        elif text_type == TextType.CODE:
            pass
        else:
            raise ValueError("Unsupported text type")