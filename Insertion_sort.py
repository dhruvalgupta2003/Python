def Insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        key=a[i]
        j=i-1
        while(key<a[j] and j>=0):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
from array import *
a=array('i',[])
n=int(input("Enter the length of the array: "))

for i in range(n):
    x=int(input("Num: "))
    a.append(x)
print("array before sorting: ",a)
Insertion_sort(a)
print("array after sorting: ",a)
