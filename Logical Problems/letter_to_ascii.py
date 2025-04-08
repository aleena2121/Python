def convert_to_dict(list_of_char):
    """
    This function coverts the given list of characters to a dictionary containing the character as the key and its ascii value as the value

    Parameters
    ---
    list_of_char: a list of letters to be converted to a dictionary

    Returns:
    dict : a dictionary with letters and their corresponding ascii values
    
    """
    dict = {}
    dict = {letter: ord(letter) for letter in list_of_char if letter not in dict}

    return dict

characters = list(map(str,input("Enter the characters: ").split()))
print(convert_to_dict(characters))