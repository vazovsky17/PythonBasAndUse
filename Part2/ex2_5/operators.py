import operator as op

# print(op.add(4, 5))
# print(op.mul(4, 5))
# print(op.contains([1, 2, 3], 4))

# x = [1, 2, 3]
# f = op.itemgetter(1)
# print(f(x))

# f = op.attrgetter("sort")
# print(f([1, 2, 3, 6, 3, 2, 1]))

x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

x.sort(key=op.itemgetter(-1), reverse=True)
print(x)
