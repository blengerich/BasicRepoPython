from config import repo_url, repo_name

for fname in ["CONTRIBUTING.md", "README.md", "setup.py"]:
    with open(fname, 'r') as f:
        text = f.read()
    text = text.replace("{repo_url}", repo_url)
    text = text.replace("{repo_name}", repo_name)

    with open(fname, 'w') as f:
        f.write(text)

import os
os.makedirs(repo_name, exist_ok=True) # Source files should be written here