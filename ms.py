def bs(arr,low,high,x):
    
    if (high >= low):
        mid = ((high + low) // 2)
            
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return bs(arr, low, mid - 1, x)
        
        else:
            return bs(arr, mid + 1, high, x)
        
    else:
        # Element is not present in the array
        return -1


fisrt = 0
book = [1,2,45,78,79,98,102,222]
last = len(book)-1
find = 2


pagenum = bs(book,fisrt,last,find)
if (pagenum == -1):
    print("shigalilla")
else:
    print(pagenum)

