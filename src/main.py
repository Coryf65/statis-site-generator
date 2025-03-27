#!/usr/bin/python3

import textnode

def main():
    print("hello world")
    node = textnode.TextNode("This is some anchor text", textnode.TextType.LINKS, "https://www.boot.dev")
    print(node)
    # TextNode(This is some anchor text, link, https://www.boot.dev)

if __name__ == '__main__':
    main()