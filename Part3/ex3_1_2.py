s, t = (input() for _ in range(2))
count = 0
for i in range(len(s)):
    if s.find(t, i, i + len(t)) >= 0:
        count += 1
print(count)