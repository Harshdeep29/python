num = int(input("Enter a number:"))
flag=0
for i in range(2,num//2):
    if(num%i==0):
        print("Not prime")
        flag=1
        break

if(flag==0):
    print("Prime")
print("Finish")
