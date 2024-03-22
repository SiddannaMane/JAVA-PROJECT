def ls(arr,x):
    for i in range(len(arr)):
        if(arr[i] == x):
            return i
        
    return -1

arr = [645,468,21,846,321,8,5,87]
x = 846
page = ls(arr,x)

print(page)