def sum_of_odd_and_even_elements(list):
    """
    This function returns a list with sum of even numbers and sum of odd numbers of the given list

    Parameters - 
    list - a list of integers

    Returns - 
    A list of 2 integers, sum of even numbers and sum of odd numbers
    """
    result = [0,0]
    for i in list:
        if i % 2 == 0:
            result[0] += i
        else:
            result[1] += i
    return result
list = list(map(int,input("Enter a list: ").split()))
print(sum_of_odd_and_even_elements(list))