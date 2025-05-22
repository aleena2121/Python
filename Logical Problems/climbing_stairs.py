def climbStairs(n):
    """
    This function returns the number of distinct ways can you climb to the top of a staircase
    
    Args:
    n: no of steps
    
    Returns:
    no of distinct ways
    """
    if n <= 2:
        return n
    dp = [0]*(n+1)
    dp[1],dp[2] = 1,2

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[-1]

print(climbStairs(3))