import random


class Stack:
    def __init__(self, size=5):
        self.__size = size
        self.__counter = 0
        self.__list = ['' for i in range(size)]

    def size(self):
        return self.__counter

    def show(self):
        print((self.__list[:self.__counter:]))

    def push(self, n):
        if self.__counter == self.__size:
            raise IndexError('list index out of range')
        else:
            self.__list[self.__counter] = n
            self.__counter += 1

    def pop(self):
        if self.__counter == 0:
            raise IndexError('list is empty')
        else:
            self.__counter -= 1


if __name__=='__main__':
    try:
        stack1 = Stack(4)
        stack1.show()
        print(stack1.size())
        for i in range(3):
            stack1.push(random.randint(1, 9))
        stack1.show()
        print(stack1.size())
    except Exception as er:
        print(er)


