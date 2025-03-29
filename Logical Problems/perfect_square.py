def perfect_square(num):
    """
    To find if the integer given is a perfect square or not
    
    Parameters:
    num: a number
    
    Returns:
    True if number is a perfect square else False
    """
    if num < 2:
        return True
    left,right = 1,num
    while left <= right:
        mid = (left+right)//2
        if mid*mid < num:
            left = mid + 1
        elif mid*mid > num:
            right = mid - 1
        elif mid*mid == num:
            return True
    return False

num = int(input("Enter a number: "))
isPerfectNumber = perfect_square(num)
if isPerfectNumber:
    print("It is a perfect number")
else:
    print("Not a perfect number")