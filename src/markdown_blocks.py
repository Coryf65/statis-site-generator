#!/usr/bin/python3

from enum import Enum


class BlockType(Enum):
    """
    An enum to represent the different types of blocks in a Markdown document.
    """
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


def block_to_block_type(block):
    """
    takes a single block of markdown text as input and returns the BlockType representing the type of block it is
    :param block: A single block of markdown text
    :return: The BlockType representing the type of block
    """
    if block.startswith("# "):
        return BlockType.heading
    elif block.startswith("`"):
        return BlockType.code
    elif block.startswith("> "):
        return BlockType.quote
    elif block.startswith("- "):
        return BlockType.unordered_list
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.ordered_list
    else:
        return BlockType.paragraph  


def markdown_to_blocks(markdown):
    """
    It takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings.
    
    :param markdown: The raw Markdown string.
    :return: A list of "block" strings.
    """
    blocks = []
    lines = markdown.split("\n\n")
    for line in lines:
        #print("line: ", line)
        if line == "":
            continue
        blocks.append(line.strip())
    return blocks