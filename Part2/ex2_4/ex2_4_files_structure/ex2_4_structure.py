import os.path

need = []
for current_dir, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py") and current_dir not in need:
            need.append(current_dir)
with open('file.txt', 'w') as w:
    w.write('\n'.join(need))
