import os
import os.path
import shutil

# print(os.listdir())
# print(os.getcwd())
# print(os.path.exists("files.py"))
# print(os.path.isfile("files.py"))
# print(os.path.isdir("files.py"))
# print(os.path.abspath("files.py"))

# print(os.getcwd())
# os.chdir(".idea")
# print(os.getcwd())

shutil.copy("text.txt", "text2.txt")

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)
