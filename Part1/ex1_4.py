mapa = {'global': {'space': [],
                   'vars': []}
        }


def create(namespace, parent):
    if namespace not in mapa:
        mapa[namespace] = {}
        mapa[namespace]['space'] = []
        mapa[namespace]['vars'] = []
        mapa[namespace]['parent'] = parent
        mapa[parent]['space'].append(namespace)
    elif 'space' not in mapa[namespace]:
        mapa[namespace]['space'] = []
        mapa[namespace]['parent'] = parent
        mapa[parent]['space'].append(namespace)
    else:
        mapa[namespace]['space'] = []
        mapa[namespace]['parent'] = parent
        mapa[parent]['space'].append(namespace)


def add(namespace, var):
    if namespace not in mapa:
        mapa[namespace] = {}
        mapa[namespace]['vars'] = []
        mapa[namespace]['vars'].append(var)
    elif 'vars' not in mapa[namespace]:
        mapa[namespace]['vars'] = []
        mapa[namespace]['vars'].append(var)
    else:
        mapa[namespace]['vars'].append(var)


def get(namespace, var):
    if var in mapa[namespace]['vars']:
        return namespace
    else:
        try:
            parent = mapa[namespace]['parent']
        except KeyError:
            return None
        return get(parent, var)


for i in range(int(input())):
    com, first, last = input().split()
    if com == 'add':
        add(command[1], command[2])
    elif com == 'create':
        create(command[1], command[2])
    else:
        print(get(command[1], command[2]))
