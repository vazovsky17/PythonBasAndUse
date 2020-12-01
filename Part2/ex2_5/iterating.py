# n, k, g = map(int, input().split())
# print(n + k - g)
#
# map_obj = map(int, [1, 2, 3])
# n = next(map_obj)
# print(n)

# x = input().split()
# xs = (int(i) for i in x)
#
# evens = filter(lambda x: x % 2 == 0, xs)
# print(*evens, sep='\n')
x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

x.sort(key=lambda name: len(' '.join(name)))
print(x)
