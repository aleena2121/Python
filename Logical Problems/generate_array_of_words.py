def anagram(name,words):
    """
    Function that checks if a given name can generate an array of words

    Args:
    name: name to check if array of words can be created from it
    words: array of words

    Returns:
    True if given name can generate an array of words, else False
    """
    if sorted("".join(n.lower() for n in name if n != " ")) == sorted("".join(word.lower() for word in words)):
        return True 
    return False

print(anagram("Chris Pratt", ["chirps", "rat"]))