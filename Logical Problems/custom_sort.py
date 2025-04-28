def custom_sort(s,t):
    """
    Function to sort the characters in s such that if the character is present 
    in t then it is sorted according to the order in t and other characters are 
    sorted alphabetically after the ones found in t
    
    Args: 
    s: to be sorted string
    t: template string

    Returns
    sorted_string: sorted string
    """
    sorted_string = ""
    for char in s:
        if char in t:
            sorted_string += char
            t = t.replace(char,"")
    sorted_string += "".join(sorted(t))
    return sorted_string

print(custom_sort("fby", "abcdefzyx"))
