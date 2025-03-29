def target_sum(nums,target):
    """
    Finds the indices of the elements with add up to the target sum

    Parameters:
    nums: a list of number
    target: the target sum that we need to search

    Returns:
    A list of the indices of the elements with add up to the target
    """
    indices = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                indices.append(i)
                indices.append(j)
    return indices

nums = list(map(int,input("Enter a list: ").split()))
target = int(input("Enter the target sum: "))
result = target_sum(nums,target)
print(result)