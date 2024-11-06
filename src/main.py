from textnode import *
from htmlnode import *

def main():
    test_dict = {"href": "https://www.google.com", "target": "_blank",}


    MyNode = TextNode("This is a test node", TextType.BOLD, "https://www.boot.dev")
    print (MyNode)
    html_node = HTMLNode("h1","this will be a header",[],test_dict)
    print (html_node)
    print (html_node.props_to_html())

main()