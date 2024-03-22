def linearsearch(arr,x):
     i=0
     while i<len(arr):
         if arr[i]==x:
             return i
         i=i+1
     return -1
arr=[45,25,68,23,15,42,98]
x=23
print(linearsearch(arr,x))
