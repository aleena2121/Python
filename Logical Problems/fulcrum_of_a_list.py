def find_fulcrum(nums):
    """
    Function that finds the fulcrum of a list
    
    Args:
    nums: a list of numbers

    Returns:
    nums[i], a number in the list, if it has the same sum to its right and left both, else -1
    """
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return nums[i]
    return -1

print(find_fulcrum([3, 1, 5, 2, 4, 6, -1]))