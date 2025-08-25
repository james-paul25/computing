class Calculator:
    def add(self, a, b):
        return a + b
    def minus(self, a, b):
        return a - b
    def multiply(self, a ,b):
        return a * b
    def divide(self, a, b):
        return a/b
    
class Input:
    cal = Calculator()
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Choose operator(+,-,*,/): ")
    
    if operator == '+':
        print(cal.add(num1, num2))
    elif operator == '-':
        print(cal.minus(num1, num2))
    elif operator == '*':
        print(cal.multiply(num1, num2))
    elif operator == '/':
        print(cal.divide(num1, num2))
    
    
class Main:
   Input()
    
    
Main()