def find_majority_element(nums):
    """
    Finds the element that appears most times

    Parameters:
    nums: a list of integers

    Returns:
    The element that appears most times in the list
    
    """
    for i in nums:
        if nums.count(i) > majority_element_count:
            majority_element_count = nums.count(i)
            majority_element = i
    return majority_element

nums = list(map(int,input("Enter a list: ").split()))
print(f"Majority element: {find_majority_element(nums)}")