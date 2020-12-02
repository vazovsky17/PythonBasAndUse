from xml.etree.ElementTree import XMLParser


# xml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'

class Colors:
    depth = 0
    weights = {'red': 0, 'green': 0, 'blue': 0}

    def start(self, tag, attrib):
        self.depth += 1
        self.weights[attrib['color']] += self.depth

    def end(self, tag):
        self.depth -= 1

    def data(self, data):
        pass

    def close(self):
        weights_list = [self.weights['red'], self.weights['green'], self.weights['blue']]
        return ' '.join(list(map(str, weights_list)))


target = Colors()
parser = XMLParser(target=target)
parser.feed(input())
print(parser.close())
'''
Введем понятие ценности для кубиков. 
Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. 
Кубики, расположенные прямо под ним, имеют ценность 2. 
Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
Ценность цвета равна сумме ценностей всех кубиков этого цвета.
Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
4 3 1
'''

'''
короткое решение
from xml.etree import ElementTree

def lvl(tr, cnt):
    a[tr.attrib['color']] += cnt
    cnt += 1
    for i in tr:
        lvl(i, cnt)
    return a

tree = ElementTree.fromstring(input())
a = {'red': 0, 'green': 0, 'blue': 0}

lvl(tree, 1)
print(a['red'], a['green'], a['blue'])
'''
