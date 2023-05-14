# 87284740
class DequePushError(Exception):
    pass


class DequePopError(Exception):
    pass


class Deque:
    def __init__(self, max_size):
        self.__buffer = [None] * max_size
        self.__front = 0
        self.__back = 0
        self.__size = 0
        self.__max_size = max_size

    def push_front(self, value):
        if self.__size == self.__max_size:
            raise DequePushError("error")
        self.__front = (self.__front - 1 +
                        self.__max_size) % self.__max_size
        self.__buffer[self.__front] = value
        self.__size += 1

    def push_back(self, value):
        if self.__size == self.__max_size:
            raise DequePushError("error")
        self.__buffer[self.__back] = value
        self.__back = (self.__back + 1) % self.__max_size
        self.__size += 1

    def pop_front(self):
        if self.__size == 0:
            raise DequePopError("error")
        value = self.__buffer[self.__front]
        self.__buffer[self.__front] = None
        self.__front = (self.__front + 1) % self.__max_size
        self.__size -= 1
        return value

    def pop_back(self):
        if self.__size == 0:
            raise DequePopError("error")
        self.__back = (self.__back - 1 + self.__max_size) % self.__max_size
        value = self.__buffer[self.__back]
        self.__buffer[self.__back] = None
        self.__size -= 1
        return value


if __name__ == '__main__':
    team_number = int(input())
    max_deq_size = int(input())
    deq = Deque(max_deq_size)

    for _ in range(team_number):
        command = input().split()
        try:
            method_name = command[0]
            method = getattr(deq, method_name)
            if len(command) > 1:
                value = int(command[1])
                if method_name == "push_front":
                    method(value)
                elif method_name == "push_back":
                    method(value)
                else:
                    raise AttributeError("Неверная команда")
            else:
                value = method()
                if value is not None:
                    print(value)
                else:
                    raise DequePopError("error")
        except AttributeError:
            print("Неверная команда")
        except (DequePopError, DequePushError) as e:
            print(e)
