def merge(arr,left,mid,right):
    """
    This function merges and sorts the list
    """
    n1 = mid - left + 1
    n2 = right - mid

    L = [0]*n1
    R = [0]*n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    
    i,j,k = 0,0,left

    # merging 
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # adding remaining elements
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr,left,right):
    """
    This function recursively divides the list into half until there is only one element
    """
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr,left,mid,right)



arr = [10,4,32,39,20,1]

print(f"Original list : {arr}")
merge_sort(arr,0,len(arr)-1)
print(f"Sorted list: {arr}")