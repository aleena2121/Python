# def sort_colors(arr):
#     for i in range(len(arr)-1):
#         min_idx = i
#         for j in range(i+1,len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         arr[min_idx],arr[i] = arr[i],arr[min_idx]
#     return arr

def partition(arr,low,high):
    pivot = arr[high]

    i = low - 1

    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1

            
def quick_sort(arr,low,high):
    if low <= high:
        p = partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)

arr = [0,1,2,1,2,2,1,0,1,2]
quick_sort(arr,0,len(arr)-1)
print(arr)