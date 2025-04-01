def find_column_numbers(col_title):
    """
    This function gives the corresponding column number for the given column title

    Parameters -
    col_title: a string representing the column title

    Returns -
    The corresponding column number
    """
    alphabets = {chr(i): i - 96 for i in range(97, 123)}     # creates a dictionary of the letters corresponding to its ascii value
    number = 0
    length = len(col_title)
    for i in col_title:
        number += alphabets[i.lower()]*(26**(length-1))
        length -= 1
    return str(number)

col_title = input("Enter the column title: ")
print(f"The correspondong column number is: {find_column_numbers(col_title)}")