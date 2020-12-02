import sys
import re

pattern = r'human'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, 'computer', line))

'''
короткое решение
print(re.sub(r'human', 'computer', sys.stdin.read()), end='')
'''
