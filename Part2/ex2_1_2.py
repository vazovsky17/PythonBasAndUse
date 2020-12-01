my_dict = {}
my_list = []

for _ in range(int(input())):
    x = input().split()
    my_dict[x[0]] = x[2:]


def found_path(dictionary, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in dictionary:
        return []
    for node in dictionary[start]:
        if node not in path:
            new_path = found_path(dictionary, node, end, path)
            if new_path:
                return new_path
    return []


commands = [input() for _ in range(int(input()))]
for throw in commands:
    for throw_dict in my_list:
        if len(found_path(my_dict, throw, throw_dict)) > 1:
            print(throw)
            break
    my_list.append(throw)

'''
Решение покороче
parents = {}
for _ in range(int(input())):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def is_parent(child, parent):
    if child == parent: return True
    for p in parents[child]:
        if is_parent(p, parent ): return True
    return False

exceptions = []
for _ in range(int(input())):
    a = input().strip()
    for i in exceptions:
        if is_parent(a,i):
            print(a)
            break
    exceptions.append(a)
'''