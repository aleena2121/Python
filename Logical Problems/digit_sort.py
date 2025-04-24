from collections import defaultdict
def digit_sort(nums):
    """
    Function that sorts a list of integers by their digit length in descending order,
    then settles ties by sorting numbers with the same digit length in ascending order
    
    Args: 
    nums: a list of integers
    
    Returns
    sorted_list: sorted list according to rules
    """
    dict_len = defaultdict(list)
    for num in nums:
        dict_len[len(str(num))].append(num)
    sorted_list = []
    sorted_keys = sorted(dict_len.keys(), reverse=True)
    for key in sorted_keys:
        sorted_list.extend(sorted(dict_len[key]))
    return sorted_list

print(digit_sort([77, 23, 5, 7, 101]))