def insertion_sort(arr):
    """
    This function performs selection sort on the given array
    """
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

arr = [10,4,32,39,20,1]

print(f"Original list : {arr}")
print(f"Sorted list: {insertion_sort(arr)}")