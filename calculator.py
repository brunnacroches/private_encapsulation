class Calculator:

    def calculate(self, op, num1, num2):
        if op == '+':
            return self.__add(num1, num2)
        elif op == '-':
            return self.__subtrair(num1, num2)
        else:
            print('Invalid Operation')
    
    def __add(self, num1, num2):
        return num1 + num2
    
    def __subtract(self, num1, num2):
        return num1 - num2

calculator = Calculator()
result = calculator.calculate('+', 3, 2)
print(result)