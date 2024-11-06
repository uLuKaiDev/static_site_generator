import unittest
from htmlnode import HTMLNode, LeafNode

test_dict = {"href": "https://www.google.com", "target": "_blank",}

class TestHTMLNode(unittest.TestCase):
    def test_empty(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1,node2)
    
    def test_to_html_props(self):
        node = HTMLNode("div",
                        "Hello World!", 
                        None, 
                        {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"'
        )
    
    def test_values(self):
        node = HTMLNode(
            "div",
            "This will be a test value",
        )
        self.assertEqual(
            node.tag, "div"
        )
        self.assertEqual(
            node.value, "This will be a test value"
        )
        self.assertEqual(
            node.children, None
        )
        self.assertEqual(
            node.props, None
        )
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "Hello World",
            None,
            {"class": "primary"}
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, Hello World, children: None, {'class': 'primary'})"
        )

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.__repr__(),
            "LeafNode(a, Click me!, children: None, {'href': 'https://www.google.com'})"
        )
    
    def test_to_html(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")