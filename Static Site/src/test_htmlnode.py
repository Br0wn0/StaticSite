import unittest
from htmlnode import HTMLnode, LeafNode, ParentNode

class TestHTMLnode(unittest.TestCase):
    def test_props_to_html(self):
        props = {"href": "https://www.runescape.com", "target": "_blank"}
        node = HTMLnode(props=props)
        expected_output =' href="https://www.runescape.com" target="_blank"'

        self.assertEqual(node.props_to_html(), expected_output)
class TestLeafNode(unittest.TestCase):
    def test_leaf(self):
       node = LeafNode("p", "sup, nerd!")
       self.assertEqual(node.to_html(), "<p>sup, nerd!</p>")
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
class TestParentNode(unittest.TestCase):
    def test_parent(self):
        node = ParentNode(
            "p", 
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic markers baby"),
            ],
    )
        self.assertEqual(node.to_html(),"<p><b>Bold Text</b>Normal text<i>italic markers baby</i></p>")


if __name__ == "__main__":
    unittest.main()