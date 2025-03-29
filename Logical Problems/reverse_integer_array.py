def reverse_array(nums):
    """
    Reverses the array given

    Parameters:
    nums: a list of integers

    Returns:
    Reversed array
    """
    reversed_array = []
    for i in range(len(nums)-1,-1,-1):           # can be done through slicing also
        reversed_array.append(nums[i])           # return nums[::-1]
    return reversed_array

nums = list(map(int,input("Enter a list: ").split()))
print(f"Reversed array: {reverse_array(nums)}")
