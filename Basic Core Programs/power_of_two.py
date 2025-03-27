def power_of_two(n):
    """
    Fucntion to print powers of 2 upto 2^n

    Parameters:
    n : an integer

    Returns:
    Prints all the powers of 2 upto 2^N
    """
    for i in range(n+1):
        print(pow(2,i))
    
n = int(input())
if n<0 or n>31:
    print("Invalid Input")
else:
    power_of_two(n)