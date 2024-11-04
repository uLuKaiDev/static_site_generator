from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url= None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other_node):
        return self.__dict__ == other_node.__dict__
    
    def __repr__(self):
        return (f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})")
    