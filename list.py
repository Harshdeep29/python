lst=[]
for i in range(0,10):
    lst.append(int(input("Enter a number:")))
print(lst)
for j in range(len(lst)):
    for k in range(len(lst)):
        if(lst[j]<lst[k]):
            '''c=lst[j]
            lst[j]=lst[k]
            lst[k]=c'''
            lst[j],lst[k]=lst[k],lst[j]
print(lst)
