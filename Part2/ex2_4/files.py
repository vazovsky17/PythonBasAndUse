f = open("text.txt", "r")
for line in f:
    line = line.strip()
    print(repr(line))
x = f.read()
print(repr(x))
f.close()
