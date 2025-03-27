def harmonic_number(n):
    """
    Returns the nth harmonic number 

    Parameters:
    n: an integer

    Returns:
    Prints the nth harmonic number
    """
    sum = 0
    for i in range(1,n+1):
        sum += (1/i)
    return sum

n = int(input())
if n == 0:
    print("Invalid Input")
else:
    print(harmonic_number(n))