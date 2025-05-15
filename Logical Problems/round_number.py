def round_number(num,n):
    """
    This function takes two integers, num and n, and returns an integer which is divisible by n and is the closest to num
    
    Args: 
    num, n : integers

    Returns:
    x : integer which is divisible by n and is the closest to num
    """
    lower = (num // n) * n
    upper = lower + n

    if abs(num - lower) == abs(upper - num):
        return upper 
    elif abs(num - lower) < abs(upper - num):
        return lower
    else:
        return upper


print(round_number(33, 25))