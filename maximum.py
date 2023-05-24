'''a=int(input("Enter a number: "))
if(a&1==0):
    print("Number is even")
else:
    print("Number is odd")
a=float(input("Enter your percentage: "))
if(a>=90):
    print("A+")
elif(90>a>80):
    print("A")
elif(80>=a>=65):
    print("B")
else:
    print("You are fail")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a>b):
    if(a>c):
        print(a,"is the largest")
    else:
        print(c,"is the largest")
else:
    if(b>c):
        print(b,"is the largest")
    else:
        print(c,"is the largest")
'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a>b) and (a>c):
    print(a,"is the largest")
elif(b>a) and (b>c):
    print(b,"is the largest")
elif(c>a) and (c>b):
    print(c,"is the largest")
