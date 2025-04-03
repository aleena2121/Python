def last_digit(a,b,c):
    """
    This function returns true or false based on if the product of last digit of first 2 numbers is equal to the last digit of the third number
    
    Parameters
    ---
    a,b,c : three numbers to check the last digits

    Returns
    ---
    True if last digit of a * last digit of b = last digit of c else False
    """
    return ((a % 10) * (b % 10)) % 10 == (c % 10)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(last_digit(a,b,c))