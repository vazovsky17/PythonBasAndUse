class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return f"Hello, {name}"
    else:
        raise BadName(f"{name} is inappropriate name")


print("import is execution")
