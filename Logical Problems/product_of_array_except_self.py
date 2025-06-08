from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    This function returns a list which has the product of elements exept itself

    Args: 
    nums: a list of integers

    Returns:
    answer: a list of integers(the products)
    """
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    answer = [prefix[i] * suffix[i] for i in range(n)]
    return answer


print(productExceptSelf([1,2,3,4]))