from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    """
    This function returns the number of elements after removing the duplicates
    
    Args:
    nums: a list of integers
    
    Retuerns:
    k: number of elements after removing duplicates
    """
    k = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1 
    return k


print(removeDuplicates([1,1,1,2,2,3]))