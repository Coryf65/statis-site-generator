import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_a_leaf_was_created(self):
        leaf = LeafNode("h1", "Title")
        should = "<h1>Title</h1>"
        self.assertEqual(leaf.to_html(), should)
        
    def test_leaf_with_no_value_has_valueError(self):
        self.assertRaises(Exception, LeafNode("p", None))
        
    def test_leaf_with_no_tag_returns_the_value(self):
        value = "returns just this"
        leaf = LeafNode(None, value)
        self.assertEqual(value, leaf.value)
        
    def test_converts_to_html_ps_correctly(self):
        answer = "<p>This is a paragraph of text.</p>"
        leaf = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(answer, leaf)

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()