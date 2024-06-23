import numpy as np
n=list((input("Enter the array elements")))
a=np.array(n)
print(a)
for i in range(0,len(a)):
    for j in range(0,len(a)-1):
        if(a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in range(0,len(a)):
    print(a[i])
