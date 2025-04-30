def selection_sort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min_idx]):
                min_idx=j
        arr[min_idx],arr[i]=arr[i],arr[min_idx] 
    return arr           

arr=[43,75,23,12,83]
print("Original array:",arr)
sorted_arr=selection_sort(arr)
print("\n")
print(sorted_arr)