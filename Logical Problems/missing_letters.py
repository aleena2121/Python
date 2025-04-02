def get_missing_letters(string):
    """
    This function returns a string of letter not in the given string

    Parameters - 
    string: user input string

    Returns:
    missing_letters: a string containing the missing letters
    """
    missing_letters = ""
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabets:
        if letter not in string.lower():
            missing_letters += letter
    return missing_letters
    
string = input("Enter a string: ")
print(get_missing_letters(string))