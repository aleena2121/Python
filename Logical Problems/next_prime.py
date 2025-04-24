def next_prime(num):
    """
    Function to find the next prime number
    """
    def is_prime(n):
        """
        Function to check if the given number is prime or not
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    while not is_prime(num):
        num += 1
    return num 

print(next_prime(24))