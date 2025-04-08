def sort_positives(nums):
    """
    This function sorts only the positive numbers in the list and keeps the negative numbers at the same position
    
    Parameters
    ---
    num : a list of positive and negative numbers

    Return 
    ---
    positives_sorted_list : a list where all positive numbers are sorted
    """
    positives = [i for i in nums if i>0]
    positives.sort(reverse=True)

    positives_sorted_list = []

    for i in nums:
        if i > 0:
            positives_sorted_list.append(positives.pop())
        else:
            positives_sorted_list.append(i)
    return positives_sorted_list

print(sort_positives([6, 3, -2, 5, -8, 2, -2]))