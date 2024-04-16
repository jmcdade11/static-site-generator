import re

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
