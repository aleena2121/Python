def expand_string(txt):
    """
    This function takes a string txt and expands it

    Args:
    txt: a string containing numbers and alphabets

    Returns:
    expanded : expanded string
    """
    i = 0
    digits = ["1","2","3","4","5","6","7","8","9"]
    expanded = ""
    while i < len(txt):
        if txt[i] in digits:
            num = int(txt[i])
        else:
            expanded +=  (txt[i]*num)
        i += 1
    return expanded


print(expand_string("3M123u42b12a"))