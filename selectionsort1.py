def selection_sort(arr):
    i=0
    while i<len(arr):
        j=i
        k=i+1
        while k<len(arr):
            if arr[k] < arr[j]:
                j=k
            k=k+1
        arr[i],arr[j]=arr[j],arr[i]
        i=i+1
arr1=[21,23,41,52,15,42,15,13,5]
selection_sort(arr1)
print("sorted array using selection  sort method",arr1) 