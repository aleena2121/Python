def is_char_at_center(s):
    """
    Function to check whether the character is positioned in the very centre of the string or not

    Args:
    s: a string containing spaces and a character

    Returns:
    True or False
    """
    non_space_index = -1
    for i, char in enumerate(s):
        if char != ' ':
            non_space_index = i
            break
    left_spaces = non_space_index
    right_spaces = len(s) - non_space_index - 1
    return left_spaces == right_spaces

print(is_char_at_center(" # "))     