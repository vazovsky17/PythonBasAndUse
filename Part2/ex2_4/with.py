with open("text.txt") as f, open("text_copy.txt", "w") as w:
    for line in f:
        w.write(line)
