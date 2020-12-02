import sys
import re

pattern = r'\b[aA]+\b'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, 'argh', line, count=1))
