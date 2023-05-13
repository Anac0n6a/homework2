stack = []
operators = ["+", "-", "*", "/"]

# Чтение входных данных
expression = input().split()

# Обработка входной строки
for value in expression:
    if value not in operators:
        stack.append(int(value))
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        if value == "+":
            result = op1 + op2
        elif value == "-":
            result = op1 - op2
        elif value == "*":
            result = op1 * op2
        elif value == "/":
            result = op1 // op2  # целочисленное деление
        stack.append(result)

# Вывод результата
print(stack.pop())
