import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        if old_node.text.count(delimiter) % 2 != 0:
            raise Exception(f"{old_node.text} is invalid Markdown syntax")
        else:
            split = old_node.text.split(delimiter)
            for i in range(0,len(split)):
                if split[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(split[i], text_type_text))
                else:
                    new_nodes.append(TextNode(split[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)