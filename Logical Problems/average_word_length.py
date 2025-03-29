import string
def remove_punctuations(sentence):
    """
    Removes all the punctioation from the string

    Parameters:
    sentence: a string containing words, spaces and punctiations

    Returns:
    a string which contains only words after removing all the punctuations
    """
    s = ''.join(char if char not in string.punctuation else " " for char in sentence)
    s = s.split()
    return s

def find_average_length(words):

    """
    Finds the average word length in all the words in thr given list

    Parameters;
    words: a list of all the words extracted from the string

    Returns:
    The average length of the words    
    """
    sum_of_lengths = 0
    for i in words:
        sum_of_lengths += len(i)
    
    return sum_of_lengths/len(words)


sentence = input("Enter string: ")
words = remove_punctuations(sentence)
print("Average word length: ", end="")
print(find_average_length(words))
