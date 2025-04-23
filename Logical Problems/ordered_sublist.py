def is_ordered_sublist(smlst,biglst):
    """
    Function to check if the given small list is an ordered sublist of big list
    
    Args: 
    smlst: small list of numbers
    biglst: bigger list of numbers
    
    Returns:
    True or False
    """
    j = 0
    for i in range(len(biglst)):
        if j<len(smlst) and biglst[i] == smlst[j]:
            j += 1
    if j == len(smlst):
        return True
    return False

print(is_ordered_sublist([5, 3, 1], [1, 2, 3, 4, 5]))