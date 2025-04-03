def fibonacci(num,length):
    """
    This function returns the fibonacci series for a given length

    Parameters
    ---
    num: the list in which numbers are to be added
    length: the lenght of the final list

    Returns:
    Recursivly calls the same function until the desired length is reached and then the list is returned
    """
    num.append(num[-1] + num[-2])
    if len(num) == length:
        return num
    return fibonacci(num,length)

num = [0,1] 
length = int(input("Enter length of series: "))
print(fibonacci(num,length))