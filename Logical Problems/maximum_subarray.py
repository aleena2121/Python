from typing import List


def maxSubArray(nums: List[int]) -> int:
    """
    This function returns the maximum subarray sum possible in the given list

    Args:
    nums: a list of integers

    Returns:
    max_sum: the maximum sum found
    """
    sum_so_far = 0
    max_sum = nums[0]
    for i in range(len(nums)):
        if sum_so_far < 0:
            sum_so_far = 0
        sum_so_far += nums[i]
        max_sum = max(max_sum, sum_so_far)
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))