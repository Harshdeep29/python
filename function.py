def add():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print(num1+num2)

def sub():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print(num1-num2)

choice = int(input("Enter your choice : 1. Addition \n 2. Subtraction"))
if choice==1:
    add()
if choice==2:
    sub()
