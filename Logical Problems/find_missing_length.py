def find_missing_length(list_of_lists):
    """
    Function that takes a list of lists and return the length of the missing list

    Args: 
    list_of_lists: a list containing multiple lists

    Returns:
    missing_length: missing length in list
    """
    lengths = [len(li) for li in list_of_lists]
    for i in range(min(lengths),max(lengths)):
        if i == 0:
            return False
        if i not in lengths:
            return i
    return False

print(find_missing_length([[4, 4, 4, 4], [1], [3, 3, 3]]))