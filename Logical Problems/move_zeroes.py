def move_zeroes(nums):
    """
    Moves all zeroes to the last

    Parameters:
    nums: a list of integers

    Returns:
    The same list but with all zeroes shifted to the last
    
    """
    i = 0
    count_of_zeroes = nums.count(0)
    while i<len(nums):
        if nums[i] == 0 and count_of_zeroes != 0:
            nums.remove(0)
            nums.append(0)
            count_of_zeroes -=1
        else:
            i+=1
    return nums

nums = list(map(int,input("Enter a list: ").split()))
print(f"List after moving zeroes: {move_zeroes(nums)}")