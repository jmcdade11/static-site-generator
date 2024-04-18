from textnode import TextNode
from block_markdown import markdown_to_html_node

def main():
    #dummy = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #print(dummy)

    md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
    node = markdown_to_html_node(md)
    print(node)

if __name__ == '__main__':
    main()