def is_shuffled_well(nums: list)-> bool:
    """
    Function to check it the given list is shuffled sufficiently enough or not
    
    Args:
    nums: a list of shuffled numbers

    Returns:
    True if well shuffled else false
    """
    for i in range(len(nums)-3):
        if (nums[i]+2 == nums[i+1]+1 == nums[i+2]) or (nums[i]-2 == nums[i+1]-1 == nums[i+2]):
            return False 
    return True

print(is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))