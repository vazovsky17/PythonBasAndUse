def repl(s, a, b, count=0):
    if a in b and a in s:
        return 'Impossible'
    if s == s.replace(a, b):
        return count
    else:
        count += 1
        s = s.replace(a, b)
        return repl(s, a, b, count)


print(repl(*(input() for _ in range(3))))
