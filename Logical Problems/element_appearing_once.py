def find_element_appearing_once(nums):
    """
    Finds the only element in the list that appears once

    Parameters:
    nums: a list of integers

    Returns:
    the element that appears only once
    """
    for i in nums:
        if nums.count(i) == 1:
            return i

nums = list(map(int,input("Enter a list: ").split()))
print(f"Element appearing once in the list: {find_element_appearing_once(nums)}")