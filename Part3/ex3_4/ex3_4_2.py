import json

json_file = json.loads(input())
all_names = {item['name']: set() for item in json_file}

for item_json in json_file:
    for name in all_names:
        if name in item_json['parents']:
            all_names[name].add(item_json['name'])


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


for item in sorted(all_names.keys()):
    print(f'{item} : {len(dfs(all_names, item))}')

'''
короткое решение
import json

def test(x, c):
    for i in z:
        if x in i['parents']:
            c.add(i['name'])
            c = test(i['name'], c)
    return (c)

z = json.loads(input())
z.sort(key=(lambda x: x['name']))
for i in z:
    print(i['name'], ':', len(test(i['name'], c = set()))+ 1)
'''
