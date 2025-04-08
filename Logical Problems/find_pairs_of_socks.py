from collections import Counter

def find_pairs(socks):
    """
    This function returns the number of pairs of socks found in the list

    Parameters
    ---
    socks : a list of the available socks

    Returns
    ---
    pairs : number of pairs found
    """
    s = Counter(socks)
    pairs = 0
    for sock_count in s.values():
        pairs += sock_count//2
    return pairs

socks = [1, 2, 1, 2, 1, 3, 2]
print(find_pairs(socks))