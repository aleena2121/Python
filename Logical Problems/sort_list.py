def sort_list(nums,order):
    """
    This function sorts the given list according to the order given.
    
    Parameters
    ---
    nums : a list of numbers
    order : the order in which the list is to be sorted - asc, desc or none 

    Returns
    ---
    nums : sorted list according to the order given
    """

    if order == "None":
        return nums
    elif order.lower() == "asc":
        return sorted(nums)
    elif order.lower() == "Des":
        return sorted(nums,reverse=True)
    else:
        return "Order not defined"

print(sort_list([4, 2, 3, 1], "Des" ) )