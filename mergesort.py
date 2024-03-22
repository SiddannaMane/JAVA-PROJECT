import random
def mergesort(arr):
    if (len(arr))>1:
        mid=int(len(arr)/2)
        l=arr[:mid]
        y=len(l)
        r=arr[mid:]
        z=len(r)
        mergesort(l)
        mergesort(r)
        i=0
        j=0
        k=0
        while i<y and j<z:
            if l[i]<=r[j]:
                arr[k]=l[i]
                i=i+1
                k=k+1
            elif l[i]> r[j]:
               arr[k]=r[i]
               j=j+1
               k=k+1
        while i<y:
            arr[k]=l[i]
            k=k+1
            i=i+1
        while j<z:
            arr[k]=r[j]
            k=k+1
            j=j+1
arr=[]
n=int(input("enter the no of element:"))
for i in range(n):
    num=random.randint(1,99)
    arr.append(num)
    print("before the sort")
    print(arr)
    mergesort(arr)
    print("list the sorted")
    print(arr)