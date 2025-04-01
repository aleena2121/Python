def reverse_vowels(string):
    """
    This function reverses the vowels in the string.

    Parameters:
    string: a string for which the vowels have to be reversed

    Returns:
    A new string with reversed vowels
    """
    new_string = ""
    vowels = ["a","e","i","o","u"]
    vowels_found = []
    for i in string:
        if i.lower() in vowels:
            vowels_found.append(i)
    for i in string:
        if i.lower() in vowels:
            if i.isupper():
                new_string += vowels_found[-1].upper()
            else:
                new_string += vowels_found[-1].lower()
            vowels_found.pop()
        else:
            new_string += i
    return new_string

s = input("Enter a string: ")
print(reverse_vowels(s))