from typing import List


def findDifferentBinaryString(nums: List[str]) -> str:
    """
    This function finds a binary number which is not in the list

    Args:
    nums : a list of binary numbers

    Returns:
    ans : a binary number which is not present in nums
    """
    n = len(nums)
    ans = []
    for i in range(n):
        digit = nums[i][i]
        if digit == "1":
            ans.append("0")
        else:
            ans.append("1")
    return "".join(ans)


print(findDifferentBinaryString(["111","011","001"]))