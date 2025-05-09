def partition(arr,low,high):
    """
    This function sorts all the elements less than pivot to the left of it and elements greater to the right
    """
    pivot = arr[high]  # selecting pivot as the last element
    i = low - 1   # before start of the subarray

    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j], arr[i]  # swapping all smaller elements to the left
    arr[i+1], arr[high] = arr[high], arr[i+1]  # swapping pivot to the right of smaller elements
    return i+1 # returning position of pivot

def quick_sort(arr,low,high):
    """
    This function recursively calls the function to find the pivot and sort accordingly
    """
    if low < high:
        p = partition(arr, low, high)  # getting position of pivot
        # recursive calls to left and right partitions of pivot
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


arr = [10,4,32,39,20,1]

print(f"Original list : {arr}")
quick_sort(arr,0,len(arr)-1)
print(f"Sorted list: {arr}")