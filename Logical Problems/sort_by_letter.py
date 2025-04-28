def sort_by_letter(lst):
    """
    Function that sorts each string in a list by the letter in alphabetic ascending order.

    Args:
    lst: list of strings

    Returns: 
    ordered_lst: ordered list of strings
    """
    dictionary = {}
    for s in lst:
        for char in s:
            if char.isalpha():
                dictionary[char] = s

    sorted_keys = sorted(dictionary.keys())
    ordered_lst = [dictionary[key] for key in sorted_keys]
    return ordered_lst

print(sort_by_letter(["932c", "832u32", "2344b"]))