import time
import numpy as np
import matplotlib.pyplot as plt
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] =arr[j]
            j=j-1
        arr[j+1]=key
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
    insertion_sort(arr)
    end=time.time()
    times.append(end-start)
    print("list after insertion_sort of",x+1,"element")
    print(arr)
    print("time taken for insertion_sort",n,"elements is",end-start)
    print(numtimes)
    print(times)
plt.xlabel('list length')
plt.ylabel('time complexity')
plt.plot(numtimes,times,label="insertion")
plt.grid()
plt.legend()
plt.show()