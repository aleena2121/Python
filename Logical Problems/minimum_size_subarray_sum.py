def minSubArrayLen(target, nums):
    """
    This function returns the minimum length of the subarray that has sum greater than or equal to target

    Args:
    target: an integer
    nums: a list of integers

    Returns:
    min_len: min length of subarray
    """
    left, right = 0, 0
    curr_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_len = min(min_len, right-left+1)
            curr_sum -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len