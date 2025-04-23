def factorial_of_factorial(num):
    """
    Function to return factorial of factorial of a number
    
    Args:
    num: an integer

    Returns:
    factorial of factorials of nums
    """
    def factorial(n):
        """
        Function to return factorial of a number

        Args:
        n: an integer

        Returns:
        factorial of n
        """
        if n == 0:
             return 1
        else:
            return n * factorial(n - 1)
    if num == 0:
         return 1
    else:
        return factorial(num)*factorial_of_factorial(num-1)
    

print(factorial_of_factorial(4))