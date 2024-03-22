import time
import numpy as np
import matplotlib.pyplot as plt

def Binarysearch(a, n, x):
    for i in range(0, n):
        if a[i] == x:
            return i
    return -1

times = []
a = []
numtimes = []

for i in range(1, 8):
    start = time.time()
    n = int(input("Enter the number of elements: "))
    numtimes.append(n)
    for x in range(n):
        a.append(n)
        print("List before searching", x + 1, "elements:")
        print(a)
        Binarysearch(a, n, x)
        end = time.time()
        times.append(end)
        print("List after Binarysearch of", x + 1, "elements:")
        print(a)
        print("Time taken for Binarysearch for", n, "elements is", end - start)

print(numtimes)
print(times)

plt.plot(numtimes, times, label="linear search")
plt.grid()
plt.legend()
plt.show()
