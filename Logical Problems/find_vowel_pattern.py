import re

def find_pattern(sentence):
    """
    This function finds if if any two adjacent words have this property:
    One word ends with a vowel, while the word immediately after begins with a vowel
    
    Args:
    sentence : sentence to find pattern in

    Returns:
    True if pattern found else False 
    """
    pattern_found = re.search(r"[aeiou]\s[aeiou]",sentence)
    return True if pattern_found else False

print(find_pattern("a very large appliance"))