"""
Builds the repo by reading config and replacing placeholders.
"""
import os

from config import REPO_URL, REPO_NAME

for fname in ["CONTRIBUTING.md", "README.md", "setup.py"]:
    with open(fname, 'r', encoding='UTF-8') as f:
        text = f.read()
    text = text.replace("{repo_url}", REPO_URL)
    text = text.replace("{repo_name}", REPO_NAME)

    with open(fname, 'w', encoding='UTF-8') as f:
        f.write(text)

os.makedirs(REPO_NAME, exist_ok=True)  # Add your source files to this directory.
