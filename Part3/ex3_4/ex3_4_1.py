import csv
from collections import Counter

with open('Crimes.csv') as f:
    reader = list(csv.reader(f))[1:]
    c = Counter(list(zip(*reader))[5]).most_common(1)
    print(c[0][0])
