# 87284129	
# вообще все пришлось переделывать, все ломается и не проходит тесты
class CustomNoItemsException(Exception):
    def __init__(self):
        pass

class Stack:
    def __init__(self):
        self.__data=[]
        
    def push(self,element):
        self.__data.append(element)
    
    def pop(self):
        if len(self.__data)==0:
            raise CustomNoItemsException
        else:
            return self.__data.pop()

def calculate(input_string):
    dictionary={
    '+':lambda x,y:x+y,
    '-':lambda x,y:y-x,
    '*':lambda x,y:x*y,
    '/':lambda x,y:y//x
    }
    operands = Stack()
    for val in input_string.split(' '):
        try:
            operands.push(int(val))
        except ValueError:
            operands.push(dictionary[val](operands.pop(),operands.pop()))
    
    return operands.pop()

if __name__ == '__main__':
    print(calculate(input()))
