from collections import Counter


def pluralize_words(words):
    """
    This functions pluralizes the words occuring more than once and returns the list

    Parameters
    ---
    words : a list of words

    Returns
    ---
    pluralized_words : a list of pluralized words 
    """
    word_count = Counter(words)
    pluralized_words = {word + "s" if count > 1 else word for word, count in word_count.items()}
    return pluralized_words

print(pluralize_words(["cow", "pig", "cow", "cow"]))