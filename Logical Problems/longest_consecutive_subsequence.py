from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
        """
        This function returns the longest consecutive sequence of numbers in the list

        Args:
        nums: list if integers

        Returns
        max_len: maximum lenght of consecutive sequence of numbers found
        """
        numSet = set(nums)
        max_len = 0
        for i in numSet:
            if (i - 1) not in numSet:
                length = 0
                while (i + length) in numSet:
                    length += 1
                max_len = max(length, max_len)
        return max_len

print(longestConsecutive([100,4,200,1,3,2]))