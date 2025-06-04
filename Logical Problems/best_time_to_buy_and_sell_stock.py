from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    This function gives the maximum profit which can be achieved by buying and selling stocks
    
    Args:
    prices: a list of integers denoting day wise stock prices

    Returns:
    profit: a integer deoting maximum profit which can be gained by byuing and selling stocks
    """
    profit= 0
    for i in range (1,len(prices)):
        if(prices[i] > prices[i-1]):
            profit+= prices[i] - prices[i-1]
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))