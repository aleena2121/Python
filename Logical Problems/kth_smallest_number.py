def kth_smallest_number(nums,k):
    """
    This function returns the kth smallest number in the given list

    Parameters:
    nums: a list of integers
    k: kth smallest integer to find

    Returns:
    The kth smallest integer
    """
    while k!=0:
        smallest_number = min(nums)
        nums.remove(smallest_number)
        k-=1
    return smallest_number
nums = list(map(int,input("Enter a list: ").split()))
k = int(input("Enter k: "))
print(kth_smallest_number(nums,k))