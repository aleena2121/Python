def subsets(nums):
    """
    This function returns the power set for a given list
    
    Args:
    nums: a list of integers
    
    Returns
    res : a list of lists containing the power set
    """
    res = []
    subsets = []

    def dfs(i):
        if i >=len(nums):
            res.append(subsets.copy())
            return
        
        subsets.append(nums[i])
        dfs(i+1)

        subsets.pop()
        dfs(i+1)
    
    dfs(0)
    return res