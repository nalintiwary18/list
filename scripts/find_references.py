import os, glob

terms = ['agri10x', 'blend', 'defer.run', 'toplyne', 'customerglu', 'blusmart', 'dyte', 'cacheflow', 'togai', 'protect ai', 'codeium', 'highlight.io', 'memfold', 'invoid']

for root, dirs, files in os.walk('.'):
    if '.git' in root or '__pycache__' in root or '.kilo' in root:
        continue
    for file in files:
        if file.endswith(('.json', '.csv', '.py', '.txt', '.md', '.html', '.js')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    found = [t for t in terms if t in content.lower()]
                    if found:
                        print(f"File {filepath}: found {found}")
            except Exception as e:
                pass
