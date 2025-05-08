def bubble_sort(arr):
    """
    This function performs bubble sort on the given list
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True 
        if swapped == False:   # early exit from loop if no swapping
            break 
    return arr

arr = [10,4,32,39,20,1]
print(f"Original list : {arr}")
print(f"Sorted list: {bubble_sort(arr)}")