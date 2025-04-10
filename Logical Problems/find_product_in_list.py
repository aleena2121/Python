def find_product(nums,product):
    """
    This function finds the index of the numbers in the list which result to the given product

    Parameters
    ---
    nums: a list of numbers
    product: the product to be found within the list

    Returns 
    ---
    A list of the elements which have product equal to the given number or -1 if not found
    """
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]*nums[j] == product:
                return ([nums[i],nums[j]])
    return -1
            
print(find_product([1, 2, 3, 4, 13, 5], 39)) 