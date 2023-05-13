# 87261450
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def evaluate(self, expression):
        stack = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a // b,
        }
        for value in expression:
            if value not in operators:
                stack.append(int(value))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                result = operators[value](op1, op2)
                stack.append(result)
        return stack[-1]


if __name__ == '__main__':
    stack = Stack()
    expression = input().split()
    print(stack.evaluate(expression))
