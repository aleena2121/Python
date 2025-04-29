def find_pairs(nums):
    """
    Function that pairs the first number in an array with the last, the second
    number with the second to last, etc

    Args: 
    nums: a list of numbers

    Returns:
    pairs: list of pairs
    """
    if len(nums) == 0:
        return []
    i,j = 0,len(nums)-1
    pairs = []
    while i<j:
        pairs.append([nums[i],nums[j]])
        i+=1
        j-=1
    if i==j:
        pairs.append([nums[i],nums[j]])
    return pairs

print(find_pairs([1, 2, 3, 4, 5, 6, 7]))