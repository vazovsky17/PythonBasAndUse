from lxml import etree
import requests

res = requests.get('https://docs.python.org/3')
print(res.status_code)
print(res.headers['Content-Type'])

parser = etree.HTMLParser()
root = etree.fromstring(res.text, parser)
# root = etree.XML("")

for el in root.iter('a'):
    print(el, el.attrib)
