import re

pattern = r'(test)*'
string = 'test'
match = re.match(pattern, string)
print(match)
