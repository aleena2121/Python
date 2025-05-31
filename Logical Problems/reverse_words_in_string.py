def reverseWords(s: str) -> str:
    """
    This function reverses the words in a string
    
    Args:
    s: a string

    Returns:
    s: reversed string
    """
    s_ = s.split(" ")
    s_ = [i.strip() for i in s_ if i != '']
    return " ".join(reversed(s_))


print(reverseWords("the sky is blue"))