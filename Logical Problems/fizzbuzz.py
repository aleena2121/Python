def fizzbuzz(num):
    """
    This function returns "Fizz" if the given number is divisible by 3, "Buzz" if divisible by 5 , "FizzBuzz" if divisible by both 
    and the number itself as a string is neither.

    Parameters - 
    num: an integer

    Returns - 
    "Fizz" if the given number is divisible by 3, "Buzz" if divisible by 5 , "FizzBuzz" if divisible by both 
    and the number itself as a string is neither    
    """
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)
num = int(input("Enter a number: "))
print(fizzbuzz(num))