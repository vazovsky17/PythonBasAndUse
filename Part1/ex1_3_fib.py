def fib(a):
    return 1 if a == 1 or a == 0 else fib(a-1) + fib(a-2)


print(fib(5))
