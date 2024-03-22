arr=[10,20,30,40,50,54,12]
for i in range(0,len(arr)):
        for j in range(i,len(arr),++1):
            if arr[i]> arr[j]:
                arr[j],arr[i]=arr[i],arr[j]
                
                
print("Sorted selection array:",arr)