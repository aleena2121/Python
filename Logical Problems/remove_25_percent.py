def show_the_love(nums):
    """
    Function that removes 25% from every number in the list except the smallest number, 
    and adds the total amount removed to the smallest number
    
    Args: 
    nums: a list of numbers

    Returns: 
    nums: modified list of numbers
    """
    min_num_index = nums.index(min(nums))  # getting index of minimum number in list
    for i in range(len(nums)):
        if i != min_num_index:
            nums[min_num_index] += nums[i]/4 
            nums[i] -= nums[i]/4
    return nums

print(show_the_love([16, 10, 8]) )