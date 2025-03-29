def encoding(string):
    """
    This function returns the run length of the given string

    Parameters:
    string: the string on which the encoding is to be performed

    Returns:
    returns the encoded string
    """
    letter = string[0]
    count = 0
    encoded_string = ""
    for i in range(len(string)):
        if string[i] == letter:
            count += 1
        else:
            encoded_string += str(count)+letter
            letter = string[i]
            count = 1
    encoded_string += str(count)+letter
    return encoded_string
        
string = input("Enter a string: ")
print(f"Encoded string: {encoding(string)}")