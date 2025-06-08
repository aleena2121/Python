from typing import List


def canJump(nums: List[int]) -> bool:
    """
    This function return true if you can reach the last index, or false otherwise from the first index.

    Args:
    nums: a list of integers

    Returns:
    true or false
    """
    goal = len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if i + nums[i] >= goal:
            goal = i
    
    return goal == 0


print(canJump([2,3,1,1,4]))