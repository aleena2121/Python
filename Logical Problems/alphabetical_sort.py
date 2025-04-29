import string

def is_alphabetically_sorted(sentence):
    """
    Function to check if sentence has atleast one alphabetically sorted word

    Args: 
    sentence: a string containing sentence

    Returns:
    True if there is at least one alphabetically sorted word, else False
    """
    sentence = sentence.split()
    for word in sentence:
        cleaned_word = ''.join(char for char in word if char not in string.punctuation).lower()  # removed punctuations
        if len(cleaned_word) > 2 and ''.join(sorted(cleaned_word)) == cleaned_word:
            return True
    return False 

print(is_alphabetically_sorted("The biopsy returned negative results."))