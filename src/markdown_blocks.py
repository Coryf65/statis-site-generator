#!/usr/bin/python3

from enum import Enum
from htmlnode import HTMLNode
from utilities import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from parentnode import ParentNode


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
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("`"):
        return BlockType.CODE
    elif block.startswith("> "):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.ULIST
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH


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

def markdown_to_html_node(markdown):
    """
    converts a full markdown document into a single parent HTMLNode. That one parent HTMLNode should (obviously) contain many child HTMLNode objects representing the nested elements.
    :param markdown: The raw Markdown string.
    :return: A single parent HTMLNode object containing all the child HTMLNode objects.
    """
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)