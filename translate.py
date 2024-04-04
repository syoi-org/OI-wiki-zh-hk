import opencc
import os
import sys

def list_doc_files(folder_path):
    md_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md") or file.endswith("mkdocs.yml"):
                md_files.append(os.path.join(root, file))
    return md_files

def translate_in_place(file_path, converter):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = converter.convert(content)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    if len(sys.argv) != 2:
        print("Usage: python translate.py <folder_path>", file=sys.stderr)
        sys.exit(1)
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"folder_path {folder_path} is not a directory", file=sys.stderr)
        sys.exit(1)
    converter = opencc.OpenCC('s2hk.json')
    for file_path in list_doc_files(folder_path):
        print(f"translating {file_path}...", file=sys.stderr)
        translate_in_place(file_path, converter)

if __name__ == "__main__":
    main()
