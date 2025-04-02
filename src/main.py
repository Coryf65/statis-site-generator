#!/usr/bin/python3

import textnode
import utilities
from textnode import TextNode, TextType


def main():
    # print("hello world")
    # node = textnode.TextNode("This is some anchor text", textnode.TextType.LINKS, "https://www.boot.dev")
    # print(node)
    # TextNode(This is some anchor text, link, https://www.boot.dev)
    
    # cory test
    test1 = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    result = utilities.markdown_to_blocks(test1)
    print("result: \n", result)   


if __name__ == '__main__':
    main()