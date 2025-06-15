def isCircularSentence(sentence: str) -> bool:
    """
    This function returns if the given sentence is circular or not.
    A sentence is circular if:
        The last character of each word in the sentence is equal to the first character of its next word.
        The last character of the last word is equal to the first character of the first word.

    Args:
    sentence: the given sentence

    Returns:
    True or False
    """
    words = sentence.split(" ")
    if words[0][0] != words[-1][-1]:
        return False
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return False

    return True

print(isCircularSentence("leetcode exercises sound delightful"))