import time
import numpy as np
import matplotlib.pyplot as plt
def bubblesort(arr):
    for o in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[i]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
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
    bubblesort(arr)
    end=time.time()
    times.append(end-start)
    print("list after bubble_sort of",x+1,"element")
    print(arr)
    print("time taken for bubble sort",n,"elements is",end-start)
    print(numtimes)
    print(times)
plt.xlabel('list length')
plt.ylabel('time complexity')
plt.plot(numtimes,times,label="bubblesort")
plt.grid()
plt.legend()
plt.show()