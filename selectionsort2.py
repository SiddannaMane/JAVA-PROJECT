import time
import numpy as np
import matplotlib.pyplot as plt
def selection_sort(arr):
    i=0
    while i<len(arr):
        j=i
        k=i+1
        while k <  len(arr):
            if arr[k] < arr[j]:
                j=k
            k=k+1
        arr[i],arr[j]=arr[j],arr[i]
        i=i+1
times=list()
arr=list()
numtimes=list()
for i in range(1,8):
    start=time.time()
    n=int(input("enter the no of element"))
    numtimes.append(n)
    for x in range(n):
        number=np.random.randint(10,99)
        arr.append(n)
    print("list before sorting",x+1,"element")
    print(arr)
    selection_sort(arr)
    end=time.time()
    times.append(end-start)
    print("list after selection_sort of",x+1,"element")
    print(arr)
    print("time taken for selection_sort",n,"elements is",end-start)
    print(numtimes)
    print(times)
plt.xlabel('list length')
plt.ylabel('time complexity')
plt.plot(numtimes,times,label="selection_sort")
plt.grid()
plt.legend()
plt.show()