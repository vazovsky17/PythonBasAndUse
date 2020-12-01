my_mro = {}


def add_class(name, parents):
    if name not in my_mro:
        my_mro[name] = []
    my_mro[name].extend(parents)
    for parent in parents:
        if parent not in my_mro:
            my_mro[parent] = []


for _ in range(int(input())):
    x = input().split()
    add_class(x[0], x[2:])


def where(child, parent, path=[]):
    path = path + [child]
    if child == parent:
        return path
    if child not in my_mro:
        return None
    for i in my_mro[child]:
        if i not in path:
            sec_path = where(i, parent, path)
            if sec_path:
                return sec_path
    return None


commands = [input().split() for _ in range(int(input()))]
for command in commands:
    parent, child = command
    print("No" if not (parent or child) in my_mro or not where(child, parent) else "Yes")

print(my_mro)

'''
реализация от препода
n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))

q = int(input())
for _ in range(q):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")
'''
