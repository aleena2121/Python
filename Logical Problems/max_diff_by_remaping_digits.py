def minMaxDifference(num: int) -> int:
    """
    This function returns the difference between the maximum remapped number and the minimum

    Args:
    nums : an integer

    Returns:
    difference of the numbers
    """
    num =  str(num)

    num1 = num
    for i in num1:
        if i != "9":
            num1 = num.replace(i, "9")
            break
    num2 = num
    for i in num2:
        if i != "0":
            num2 = num.replace(i, "0")
            break
        return int(num1) - int(num2)


print(minMaxDifference(11891))