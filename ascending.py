a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a>b)and(a>c):
    if(b>c):
        print(c,b,a,"are sorted in ascending order")
    else:
        print(b,c,a,"are sorted in ascending order")
if(b>a)and(b>c):
    if(a>c):
        print(c,a,b,"are sorted in ascending order")
    else:
        print(a,c,b,"are sorted in ascending order")
if(c>a)and(c>b):
    if(a>b):
        print(b,a,c,"are sorted in ascending order")
    else:
        print(a,b,c,"are sorted in ascending order")

