def reverse_integer(num):
    """
    Reverses the integer

    Parameters:
    num: an integer to reverse

    Returns:
    Reversed integer
    """
    sign = -1 if num<0 else 1
    num*=sign
    reversed_integer = 0
    while num > 0:
        x = num % 10
        num//=10
        reversed_integer = reversed_integer*10 + x
    return reversed_integer*sign


integer_to_reverse = int(input("Enter integer to reverse: "))
print(reverse_integer(integer_to_reverse))