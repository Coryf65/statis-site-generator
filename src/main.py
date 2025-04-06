#!/usr/bin/python3

import os
import sys
import shutil
from copystatic import copy_files_recursive
from generatepage import generate_pages_recursive


dir_path_static = "static"
dir_path_public = "docs" # 'public' used by regular webservers 'docs' used by github pages
dir_path_content = "content"
template_path = "template.html"
default_basepath = "/"


def main():
    
    args = sys.argv[1:]    
    
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    print(f"Deleting '{dir_path_public}' directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print(f"Copying static files to '{dir_path_public}' directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


if __name__ == '__main__':
    main()