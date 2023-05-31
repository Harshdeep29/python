lst=[]
for i in range(0,10):
    lst.append(int(input("Enter a number:")))
print(lst)
for j in range(0,10):
    for k in range(0,10):
        if(lst[j]<lst[k]):
            '''c=lst[j]
            lst[j]=lst[k]
            lst[k]=c'''
            lst[j],lst[k]=lst[k],lst[j]
print(lst)
