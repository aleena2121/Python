def unscensor(sentence,vowels):
    """
    This function replaces the "*" with the vowels given

    Parameters
    ---
    sentence : the original string containing the "*"
    vowels : a string containg vowels to be added to the sentence
    
    Returns
    ---
    a string in which "*" are replaced by the vowels
    """
    sentence = list(sentence)
    vowels = list(vowels[::-1])
    for i in range(len(sentence)):
        if sentence[i] == "*":
            sentence[i] = vowels.pop()

    return (''.join(s for s in sentence))

sentence =  "Wh*r* d*d my v*w*ls g*?"
vowels = "eeioeo"

print(unscensor(sentence,vowels))