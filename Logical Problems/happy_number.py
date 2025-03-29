def happy_number(num,seen):
    """
    The fucntion finds out if the number given is a happy number or not

    Parameters:
    num: an integer
    seen: a list to keep track of the sums found so far to avoid infinite looping

    Returns:
    True if happy number else False
    """
    new_num = sum(int(digit) ** 2 for digit in str(num))
    if new_num == 1:
        return(True)
    elif new_num not in seen:
        seen.append(new_num)
        return(happy_number(new_num,seen))
    elif new_num in seen:
        return(False)
        
num = int(input("Enter a number: "))
print(happy_number(num,[]))