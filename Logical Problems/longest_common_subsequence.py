def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    This function finds the length of the longest common subsequesnce between s and t
    
    Args:
    text1, text2: strings

    Returns:
    length of the longest common subsequence
    """
    dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

    for i in range(len(text1)-1,-1,-1):
        for j in range(len(text2)-1,-1,-1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    
    return dp[0][0]

print(longestCommonSubsequence("abcde","ace"))