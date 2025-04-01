def find_sum_of_common_integers(list1,list2,list3):
    """
    This function returns the sum of the common elements in the given 3 lists

    Parameters:
    list1,list2,list2: the lists to find the common elements from

    Returns:
    Sum of common elements    
    """
    common_elements = []
    for i in list1:
        if i in list2 and i in list3:
            common_elements.append(i)
    return str((sum(common_elements)))

list1 = list(map(int,input("Enter values for first list: ").split()))
list2 = list(map(int,input("Enter values for second list: ").split()))
list3 = list(map(int,input("Enter values for third list: ").split()))
print(f"The sum of common elements in the lists is: {find_sum_of_common_integers(list1,list2,list3)}")