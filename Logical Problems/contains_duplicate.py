def containsNearbyDuplicate(nums,k):
    """
    return true if there are two distinct indices i and j in the array 
    such that nums[i] == nums[j] and abs(i - j) <= k.

    Args:
    nums: a list of numbers
    k: an integer

    Returns:
    True or False
    """
    seen = {}
    for i,num in enumerate(nums):
        if num in seen and i - seen[num] <=k:
            return True
        seen[num] = i
    return False