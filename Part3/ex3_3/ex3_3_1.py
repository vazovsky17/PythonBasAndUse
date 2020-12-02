import requests
import re

res1 = requests.get(input())
res2 = requests.get(input())
pattern = '<a\\s.*?href="(.+?)".*?>'
lst = []
for i in re.findall(pattern, str(res1.content)):
    lst.extend(re.findall(pattern, str(requests.get(i).content)))
print("Yes" if res2.url in lst else "No")
