class Infohiding(object):
    def __init__(self):
        self.__visible__ = 'Visible'

    def printvisible(self):
        print(self.__visible__)

    def __printinvisible__(self):
        print(self.__visible__)


test1 = Infohiding()
print(test1.__visible__)
test1.printvisible()
test1.__printinvisible__()
