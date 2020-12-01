# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности
# и выводить сумму пятерок последовательных элементов по мере их накопления.
# Одним из требований к классу является то,
# что он не должен хранить в себе больше элементов,
# чем ему действительно необходимо, т. е. он не должен хранить элементы,
# которые уже вошли в пятерку, для которой была выведена сумма.

class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        for i in a:
            if len(self.lst) < 4:
                self.lst.append(i)
            else:
                self.lst.append(i)
                print(sum(self.lst))
                self.lst = []

    def get_current_part(self):
        return self.lst


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part()  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part()  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()  # вернуть [1]
