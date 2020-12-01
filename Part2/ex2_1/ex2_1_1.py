def foo(a, b):
    print(a / b)


try:
    foo()
except ZeroDivisionError as e:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")
