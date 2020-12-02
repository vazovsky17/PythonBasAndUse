# http://numbersapi.com/number
import requests

with open('file.txt', 'r') as f:
    for num in f:
        num = num.strip()
        res = requests.get(f'http://numbersapi.com/{num}/math', params={'json': True})
        print('Interesting' if res.json()['found'] else "Boring")
