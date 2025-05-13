def letters(word1, word2):
    """
    This function returns a list of three elements, in the following order:
        Shared letters between two words.
        Letters unique to word 1.
        Letters unique to word 2

    Args: 
    word1, word2 : strings

    Returns:
    a list of 3 strings
    """
    set1 = set(word1)
    set2 = set(word2)
    shared = sorted(set1.intersection(set2))
    unique_to_1 = sorted(set1 - set2)
    unique_to_2 = sorted(set2 - set1)
    return ["".join(shared), "".join(unique_to_1), "".join(unique_to_2)]

print(letters("sharp", "soap"))