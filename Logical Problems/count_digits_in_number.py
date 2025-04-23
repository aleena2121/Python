def count_digits_in_number(number):
    """
    Fucntion to count the number of digits in a number
    
    Args:
    number: an integer or float
    
    Returns:
    count: count of the digits in number
    """
    if isinstance(number, float):
        number = int(number)

    count = 0
    while number != 0:
        number = number//10
        count +=1
    return count 

print(count_digits_in_number(1e8))