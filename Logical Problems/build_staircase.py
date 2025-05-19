def build_staircase(num):
    """
    This function will build a staircase using underscore _ and hash # symbols

    Args:
    num : an integer

    Returns:
    prints the staircase
    """
    if num > 0:
        first,second = "_","#"
    else:
        first,second = "#","_"
    
    for i in range(abs(num)):
        print(f'{first*(abs(num)-i-1)}{second*(i+1)}\n')
    

build_staircase(7)