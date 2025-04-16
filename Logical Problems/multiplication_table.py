from typing import List

def create_table(n: int) -> List[List[int]]:
    """
    This function gives a nxn multiplication table

    Args: 
    n : an integer given by user

    Returns:
    table : a nxn multiplication table
    """
    table = [[i*j for i in range (1,n+1)] for j in range(1,n+1)]
    return table

print(create_table(5))
