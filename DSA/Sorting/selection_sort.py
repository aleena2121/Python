def selection_sort(arr):
    """
    This function performs selection sort on the given array
    """
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):  # selecting element with minimum value
            if arr[j] < arr[min_idx]:
                min_idx = j 
        arr[i],arr[min_idx] = arr[min_idx],arr[i]  # swaping current element with minimum value
    return arr

arr = [10,4,32,39,20,1]

print(f"Original list : {arr}")
print(f"Sorted list: {selection_sort(arr)}")