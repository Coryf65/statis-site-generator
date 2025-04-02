#!/usr/bin/python3


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