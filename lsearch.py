import time 
def linearsearch(arr,x):
     i=0
     while i<len(arr):
         if arr[i]==x:
             return i
         i=i+1
         return -1
     arr=list()
     start=time.time()
     n=int(input("enter the no of element"))
     for i in range(n):
         number=int(input("enter the element"))
         arr.append(number)
         x=int(input("enter the element to be searched"))
         r=linearsearch(arr,x)
         if r>0:
             print("element is found at",r)
         else:
             print("element is not found")
             end=time.time()
             print("time of exucation",end-start)