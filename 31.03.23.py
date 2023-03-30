import random


class Fifo:
    def __init__(self, size=5, ):
        self.__counter = 0
        self.__size = size
        self.__list = ['' for i in range(5)]

    def size(self):
        return self.__counter

    def show(self):
        print(self.__list[:self.__counter:])

    def push(self, n):
        if self.__counter == self.__size:
            raise IndexError('error')
        else:
            self.__list[self.__counter] = n
            self.__counter += 1

    def pop(self,):
        if self.__counter == 0:
            raise IndexError('error')
        else:
            for i in range(self.__counter-1):
                self.__list[i]=self.__list[i+1]
            self.__counter-=1

if __name__=="__main__":
    try:
        f = Fifo(3)
        print(f.size())
        f.show()
        for i in range(3):
            f.push(random.randint(1, 9))
        f.show()
        print(f.size())
        print(f.pop())

    except Exception as er:
        print(er)
