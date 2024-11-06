import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
            "LeafNode(a, Click me!, {'href': 'https://www.google.com'})"
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


class TestParentNode(unittest.TestCase):
    def test_valid_parent_node_with_children(self):
        child1 = LeafNode("span", "Child 1")
        child2 = LeafNode("span", "Child 2")
        parent = ParentNode("div", [child1, child2])
        expected_html = "<div><span>Child 1</span><span>Child 2</span></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_parent_node_no_tag_raises_value_error(self):
        parent_node = ParentNode(None, children=[HTMLNode(tag="div", value="Sample text")])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "Invalid tag: no tag provided.")

    def test_parent_node_no_children_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", [])
        self.assertEqual(str(context.exception), "ParentNode requires at least one child.")

    def test_nested_parent_nodes(self):
        inner_child = LeafNode("span", "Inner Child")
        inner_parent = ParentNode("div", [inner_child])
        outer_parent = ParentNode("section", [inner_parent])
        expected_html = "<section><div><span>Inner Child</span></div></section>"
        self.assertEqual(outer_parent.to_html(), expected_html)

    def test_multiple_levels_of_nesting(self):
        deep_child = LeafNode("em", "Deep Child")
        middle_child = ParentNode("strong", [deep_child])
        top_parent = ParentNode("p", [middle_child])
        expected_html = "<p><strong><em>Deep Child</em></strong></p>"
        self.assertEqual(top_parent.to_html(), expected_html)

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
