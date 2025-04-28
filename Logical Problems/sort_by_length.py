def sort_by_length(sentence):
    """
    Function that takes a string and returns a string ordered by the length of the words

    Args:
    sentence: a string containing a sentence

    Returns:
    sorted_sentence: sentence sorted by length
    """
    return " ".join(sorted(sentence.split(),key=len))

print(sort_by_length(("Have a wonderful day")))