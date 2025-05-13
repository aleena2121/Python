def number_of_swaps(arr):
    """
    This function performs bubble sort on the given list and returns the number of swaps

    Args:
    arr : a list on integers

    Returns:
    swaps : a integer denoting the number of swaps it took to sort the list
    """
    n = len(arr)
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swaps += 1
                swapped = True 
        if swapped == False:   
            break 
    return swaps

arr = [3, 9, 7, 4]

print(f"No of swaps : {number_of_swaps(arr)}")