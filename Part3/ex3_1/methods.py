# print("cabcd".find("abc"))
# print(str.find.__doc__)

# print("cabcd".index("abc"))

# s = "The man in black fled across the desert, and gunslinger followed."
# print(s.startswith(("The man in black", "The women")))

# capital = 'London is the capital of Great Britain.'
# template = '{} is the capital of {}'
# print(template.format("London", "Great Britain"))
# print(template.format("Vaduz", "Liechtenstein"))

import requests

template = "Response from {0.url} with code {0.status_code}"
res = requests.get("http://docs.python.org/3.9")
print(template.format(res))
