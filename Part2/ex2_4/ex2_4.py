with open("first.txt", "r") as r, open("second.txt", "w") as w:
    w.write('\n'.join([line.strip() for line in r][::-1]))
