from typing import List


def maxAdjacentDistance(self, nums: List[int]) -> int:
    max_diff = 0
    for i in range(len(nums)-1):
        max_diff = max(max_diff,abs(nums[i]-nums[i+1]))
    max_diff = max(max_diff,abs(nums[len(nums)-1]-nums[0]))
    return max_diff


print(maxAdjacentDistance([1,2,4]))