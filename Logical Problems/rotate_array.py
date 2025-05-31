def rotate(nums,k):
    """
    This function rotates the array k times

    Args:
    nums: a list of integers
    k: no of times to be rotate

    Returns:
    nums: rotated array in place
    """
    k = k % len(nums)
    for _ in range(k):
        num = nums.pop()
        nums.insert(0, num)

    return nums

print(rotate([1,2,3,4,5,6],3))