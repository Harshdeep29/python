def fact(num):
    factorial=1
    for  i in range(num,1,-1):
        factorial=factorial*i
    print("The factorial of {} is {}".format(num,factorial))


fact(int(input("Enter a number")))
