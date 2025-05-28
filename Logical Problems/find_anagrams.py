from collections import Counter
def findAnagrams(s,p):
    """
    This function returns the indices at which the anagrams of p exist in s
    
    Args: 
    s, p: strings
    
    Returns:
    indices: a list of integers denoting indices where anagrams are in s
    """
    count_p = Counter(p)
    indices = []
    for left in range(len(s) - len(p) + 1):
        if Counter(s[left:left + len(p)]) == count_p:
            indices.append(left)
    return indices