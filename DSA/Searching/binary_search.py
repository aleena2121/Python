def binary_search(arr,low,high,key):  
    """
    This function finds the key in the list by performing binary search
    """
    if high >= low:
        mid = low + (high - low)//2  # finding middle element

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)  # recursive call to the left of mid
        else:
            return binary_search(arr, mid + 1, high, key)  # recursive call to the right of mid
    else:
        return -1
    
arr = [1,4,29,48,50,63,83,92]
key = 48
print(f"List : {arr}")
print(f"Element {key} found at position {binary_search(arr,0,len(arr)-1,key)}")