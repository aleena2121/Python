from typing import List


def countDistinctIntegers(nums: List[int]) -> int:
    """
    This function returns the count of distince numbers after reversing all numbers in the list

    Args:
    nums : a list of integers

    Returns:
    length of distinct set of numbers
    """
    nums_set = set(nums)
    for i in nums:
        nums_set.add(int(str(i)[::-1]))
    return len(nums_set)

print(countDistinctIntegers([1,13,10,12,31]))