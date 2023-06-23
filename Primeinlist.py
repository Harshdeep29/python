num=int(input("Enter a number:"))
flag=0
for i in range(5,50):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i)
print("Finish")
