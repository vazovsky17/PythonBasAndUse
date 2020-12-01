import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, item):
        super().append(item)
        super().log(item)


llist = LoggableList()
llist.append('Го учить Питон')
