from collections import Counter


def longestPalindrome(words):
    """
    This function returns the length of the longest palindrome that can be formed from the given words
    
    Args:
    words : a list of words

    Returns:
    length: longest palindrome which can be formed
    """
    freq = Counter(words)
    length = 0
    center_used = False

    for word in list(freq.keys()):
        rev = word[::-1]
        if word != rev:
            pair_count = min(freq[word], freq[rev])
            length += pair_count * 4
            freq[word] -= pair_count
            freq[rev] -= pair_count
        
        else:
            pair_count = freq[word] // 2
            length += pair_count * 4
            freq[word] -= pair_count * 2
            if not center_used and freq[word] > 0:
                length += 2
                center_used = True 

    return length


print(longestPalindrome(["lc","cl","gg"]))