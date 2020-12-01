class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return f"Hello, {name}"
    else:
        raise BadName(f"{name} is inappropriate name")


while True:
    try:
        name = input("Please enter your name: ")
        greeting = greet(name)
        print(greeting)
    except BadName:
        print("Please try again")
    else:
        break
