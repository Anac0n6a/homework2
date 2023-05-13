# 87239549

class Deque:
    def __init__(self, max_size):
        self.buffer = [None] * max_size
        self.front = 0
        self.back = 0
        self.size = 0
        self.max_size = max_size

    def push_front(self, value):
        if self.size == self.max_size:
            print("error")
        else:
            self.front = (self.front - 1 + self.max_size) % self.max_size
            self.buffer[self.front] = value
            self.size += 1

    def push_back(self, value):
        if self.size == self.max_size:
            print("error")
        else:
            self.buffer[self.back] = value
            self.back = (self.back + 1) % self.max_size
            self.size += 1

    def pop_front(self):
        if self.size == 0:
            return "error"
        else:
            value = self.buffer[self.front]
            self.buffer[self.front] = None
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return value

    def pop_back(self):
        if self.size == 0:
            return "error"
        else:
            self.back = (self.back - 1 + self.max_size) % self.max_size
            value = self.buffer[self.back]
            self.buffer[self.back] = None
            self.size -= 1
            return value


team_number = int(input())
max_deq_size = int(input())
deque = Deque(max_deq_size)

for i in range(team_number):
    command = input().split()
    if command[0] == "push_front":
        deque.push_front(int(command[1]))
    elif command[0] == "push_back":
        deque.push_back(int(command[1]))
    elif command[0] == "pop_front":
        value = deque.pop_front()
        if value != "error":
            print(value)
        else:
            print(value)
    elif command[0] == "pop_back":
        value = deque.pop_back()
        if value != "error":
            print(value)
        else:
            print(value)
