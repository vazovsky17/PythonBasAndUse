import sys
import re

pattern = '(1(01*0)*1|0)*'
for line in sys.stdin:
    line = line.rstrip()
    if re.fullmatch(pattern, line):
        print(line)
