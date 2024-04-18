import os
import shutil

from block_markdown import markdown_to_html_node

static_dir = "./static"
public_dir = "./public"

def main():
    print("Cleaning public directory")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    
    print("Copying static files to public directory")
    copy_content(static_dir, public_dir)
    generate_page("./content/index.md", "./template.html", "./public/index.html")

def copy_content(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    
    for file in os.listdir(source_dir):
        source_path = os.path.join(source_dir, file)
        target_path = os.path.join(target_dir, file)
        print(f"Target copy: {source_path} -> {target_path}")
        if os.path.isfile(source_path):
            print(f"Copying file: {source_path}")
            shutil.copy(source_path, target_path)
        else:
            copy_content(source_path, target_path)

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:]
    raise Exception("No h1 header provided")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.exists(from_path):
        raise ValueError(f"Path {from_path} does not exist")
    if not os.path.exists(template_path):
        raise ValueError(f"Path {template_path} does not exist")
    
    with open(from_path) as markdown_file:
        markdown_content = markdown_file.read()
    with open(template_path) as template_file:
        template_content = template_file.read()

    markdown_to_html = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", markdown_to_html)
    
    dest_path_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_path_dir):
        os.makedirs(dest_path_dir)
    with open(dest_path, "w") as dest_file:
        dest_file.write(template_content)

if __name__ == '__main__':
    main()