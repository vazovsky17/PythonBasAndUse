import re

'''
pattern = r'a[a-c]c'
string = 'acc'
match_obj = re.search(pattern, string)
print(match_obj)

string = 'abc,acc,aac'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

find_typos = re.sub(pattern, 'abc', string)  # заменяем все, что подходит под шаблон
print(find_typos)
'''

pattern = r'a[ab]+?a'
string = 'abaaba'
print(re.match(pattern, string))
print(re.findall(pattern, string))
