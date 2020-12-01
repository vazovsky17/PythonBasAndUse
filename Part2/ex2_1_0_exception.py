def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)


print(f(5, 0), end='\n\n')
print(f(5, []), end='\n\n')

try:
    15 / 0
except ZeroDivisionError:  # isinstance(e,ZeroDivisionError) == True
    print("Division by zero")


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print("result is", result)
    finally:
        print("finally")


divide(2, 1)
divide(2, 0)
divide(2, [])
