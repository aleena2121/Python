def prime_factorization(n):
    """
    Returns the prime factors of n

    Parameters:
    n: an integer

    Returns:
    A list of prime factors of n
    """
    prime_factors = []

    while n % 2 == 0:
            n = n//2
            prime_factors.append(2)
    for i in range(2,int(n**0.5)+1):
        if i % 2 != 0:
            while n % i == 0:
                n = n//i
                prime_factors.append(i)
    if n>1:
         prime_factors.append(n)
    return(prime_factors)

n = int(input())
print(prime_factorization(n))