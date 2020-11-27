#вычисляем количество различных объектов
objects = [1, 2, 3, 1, 2]

print(len(set([id(i) for i in objects])))
