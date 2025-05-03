def true_alphabetic(sentence):
    """
    Function which takes every letter in every word, and puts it in alphabetical order, while maintaining the word length

    Args: 
    sentence: a string containing a sentence

    Returns:
    sorted_sentence: sentence sorted in alphabetical order while maintaining the word length
    """
    words = sentence.split()
    length = [len(word) for word in words]
    letters = sorted("".join(words),reverse=True)
    sorted_sentence =   ""
    for l in length:
        while l:
            sorted_sentence += letters.pop()
            l-=1
        if l == 0:
            sorted_sentence += " "
    return sorted_sentence

print(true_alphabetic("edabit is awesome"))