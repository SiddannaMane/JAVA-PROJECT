import random
def partition(arr,i,j):
    pivot=arr[i]
    left=i+1
    right=j
    while True:
        while left <= right and arr[left]<pivot:
            left=left+1
        while right >=left and arr[right]>=pivot:
            right=right-1
        if left < right:
            arr[left],arr[right]=arr[right],arr[left]
        else:
            break
        arr[i],arr[right]=arr[right],arr[i]
        return right
def Quicksort(arr,i,j):
    if i>=j:
        return
    pos=partition(arr,i,j)
    
n=int(input("enter the number"))
arr=list()
for i in range(n):
    k=random.randint(10,99)
    arr.append(k)
Quicksort(arr,0,len(arr)-1)
print("sored list is",arr)        