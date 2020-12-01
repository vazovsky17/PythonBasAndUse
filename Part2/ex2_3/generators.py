from random import random


def random_generator(k):
    for i in range(k):
        yield random()


gen = random_generator(3)
print(next(gen))
print(next(gen))
print(next(gen))


def simple_gen():
    print("Checkpoint 1")
    yield 1
    print("Checkpoint 2")
    yield 2
    print("Checkpoint 3")


gen = simple_gen()
x = next(gen)
print(x)
y = next(gen)
print(y)
