def binary_search(nums,target):
    """
    To find index of target integer
    
    Parameters:
    nums: a sorted list of numbers
    
    Returns:
    The index of the target in the list
    """
    left,right = 0,len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            return mid
    return -1          # returns -1 if not found

nums = list(map(int,input("Enter a list: ").split()))
target = int(input("Enter the value to be found: "))

print(binary_search(nums,target))