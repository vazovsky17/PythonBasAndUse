import requests
import re

res = requests.get(input()).text
pattern = r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)'
for i in sorted(set(re.findall(pattern, res))):
    print(i)
