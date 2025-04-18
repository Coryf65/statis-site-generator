#!/usr/bin/python3

import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node
from utilities import extract_title


def generate_page(from_path, template_path, dest_path, base_path):
    """
    Generates a page from a template and a source file.
    
    :param from_path: The source file path.
    :param template_path: The template file path.
    :param dest_path: The destination file path.    
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # read the markdown file at from_path and store into a variable    
    with open(from_path, "r") as from_file:
        markdown_data = from_file.read()
    
    # read the template file at template_path and store into a variable    
    with open(template_path, "r") as template_file:
        template_file = template_file.read()
    
    # use markdown_to_html_node function and .to_html() method to convert the markdown file to html
    body = markdown_to_html_node(markdown_data).to_html()
    
    # use the extract_title function to grab the title
    title = extract_title(markdown_data)
    
    # replace the {{ title }} in the template with the title and the {{ content }} with the html content
    one = template_file.replace("""{{ Title }}""", title)
    converted_html = one.replace("{{ Content }}", body)
    
    # replace href="/ with href="{BASEPATH}, and src="/ with src="{BASEPATH}
    template = template.replace('href="/', 'href="' + base_path)
    template = template.replace('src="/', 'src="' + base_path)
    
    # write a new full HTML page to a file at dest_path, also create the directory if it does not exist    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(converted_html)
 
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    """
    Crawls through the directory and generates new html pages for all markdown files.
    
    :param dir_path_content: The directory path to crawl.
    :param template_path: The template file path.
    :param dest_dir_path: The destination directory path.
    """
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, base_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, base_path)