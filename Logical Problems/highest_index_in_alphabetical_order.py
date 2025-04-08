def find_highest_index(string):
    """
    This function finds the letter having the highest index value
    """
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    highest_index = float("-inf")
    for i in string:
        highest_index = max(highest_index,alphabet.index(i.lower())+1)
    return str(highest_index) + alphabet[highest_index-1]

print(find_highest_index("Andrey"))
