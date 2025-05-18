from collections import Counter

def max_frequency(sentence):
    """
    This function returns the character with the highest frequency

    Args: 
    sentence: a string containing a sentence

    Returns:
    letters: letters with highest frequency
    """
    sentence = sentence.replace(" ","")
    frequency = Counter(sentence)
    max_freq = max(frequency.values())
    most_common_chars = [char for char, freq in frequency.items() if freq == max_freq]
    return most_common_chars

print(max_frequency("Edabit"))