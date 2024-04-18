import re
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        cleaned_blocks.append(block)
    return cleaned_blocks

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode("div", children, None)

def block_to_block_type(block):
    if block_is_heading(block):
        return block_type_heading
    if block_is_code(block):
        return block_type_code
    if block_is_quote(block):
        return block_type_quote
    if block_is_unordered_list(block):
        return block_type_unordered_list
    if block_is_ordered_list(block):
        return block_type_ordered_list
    return block_type_paragraph

def block_is_heading(block):
    match = re.search("^#{1,6} .*", block)
    if match:
        return True
    return False

def block_is_code(block):
    if block.startswith("```") and block.endswith("```"):
        return True
    return False

def block_is_quote(block):
    for line in block.split("\n"):
        if not line.startswith(">"):
            return False
    return True

def block_is_unordered_list(block):
    for line in block.split("\n"):
        if not line.startswith("* ") and not line.startswith("- "):
            return False
    return True

def block_is_ordered_list(block):
    lines = block.split("\n")
    num = 1
    if not lines[0].startswith(f"{num}. "):
        return False
    for line in lines:
        if not line.startswith(f"{num}. "):
            return False
        num += 1
    return True

def block_to_html_node(block):
    type = block_to_block_type(block)
    if type == block_type_paragraph:
        return paragraph_block_to_html(block)
    if type == block_type_heading:
        return heading_block_to_html(block)
    if type == block_type_code:
        return code_block_to_html(block)
    if type == block_type_quote:
        return quote_block_to_html(block)
    if type == block_type_unordered_list:
        return unordered_list_block_to_html(block)
    if type == block_type_ordered_list:
        return ordered_list_block_to_html(block)
    raise ValueError("Invalid block type")

def heading_block_to_html(block):
    heading_size = block.count("#")
    text = block.split("#")[-1].strip()
    children = convert_text_to_children(text)
    return ParentNode(f"h{heading_size}", children)

def code_block_to_html(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = convert_text_to_children(text)
    code_parent = ParentNode("code", children)
    return ParentNode("pre", [code_parent])

def quote_block_to_html(block):
    new_lines = []
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        stripped = line.lstrip(">").strip()
        new_lines.append(stripped)
    text = " ".join(new_lines)
    children = convert_text_to_children(text)
    return ParentNode("blockquote", children)

def unordered_list_block_to_html(block):
    items = []
    lines = block.split("\n")
    for line in lines:
        text = line[2:]
        children = convert_text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)
    
def ordered_list_block_to_html(block):
    items = []
    lines = block.split("\n")
    for line in lines:
        text = line[3:]
        children = convert_text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)

def paragraph_block_to_html(block):
    lines = block.split("\n")
    text = " ".join(lines)
    children = convert_text_to_children(text)
    return ParentNode("p", children)


def convert_text_to_children(text):
    children = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children
    

