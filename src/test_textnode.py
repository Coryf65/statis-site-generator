import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_nodes_are_not_equal_when_not_equal(self):
        test1 = TextNode("None", TextType.BOLD)
        test2 = TextNode(None, TextType.BOLD)
        self.assertNotEqual(test1, test2)
        
    def test_nodes_are_equal_when_equal(self):
        test3 = TextNode("empty", TextType.CODE, "/place")
        test4 = TextNode("empty", TextType.CODE, "/place")
        self.assertEqual(test3, test4)
        
    def test_nodes_not_equal_when_text_is_different(self):
        test5 = TextNode("patrick", TextType.ITALIC)
        test6 = TextNode("rick", TextType.ITALIC)
        self.assertNotEqual(test5, test6)
        
    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()