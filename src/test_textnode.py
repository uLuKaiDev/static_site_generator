import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_eq(self):
        node = TextNode(
            "This is a text node", 
            TextType.BOLD
        )
        node2 = TextNode(
            "This is a text node", 
            TextType.BOLD
        )
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, TextType.TEXT, https://www.boot.dev)", repr(node)
        )
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type_text(self):
        text_node = TextNode(text="plain text", text_type=TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "plain text")
    
    def test_text_type_bold(self):
        text_node = TextNode(text="bold text", text_type=TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")
    
    def test_text_type_link_with_url(self):
        text_node = TextNode(text="link text", text_type=TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link text")
        self.assertEqual(html_node.props, {"href": "https://example.com"})
    
    def test_text_type_image_with_url_and_alt(self):
        text_node = TextNode(text="image alt text", text_type=TextType.IMAGE, url="https://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "image alt text"})

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError) as context:
            text_node = TextNode(text="invalid", text_type="unknown_type")
    
        self.assertEqual(str(context.exception), "Invalid text type: unknown_type")


if __name__ == "__main__":
    unittest.main()