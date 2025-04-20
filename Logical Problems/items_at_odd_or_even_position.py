from typing import Union

def get_elements(list_or_string: Union[list,str] ,specifier: str) -> Union[list,str]:
    """
    Function to get elements at the specified position

    Args:
    list_or_string: input from user to extract elements from
    specifier: even or odd 

    Returns: 
    List or string of elements at the specified position
    """
    start = 0 if specifier == "odd" else 1
    result = list_or_string[start::2]
    return result if isinstance(list_or_string, list) else ''.join(result)

list_or_string = "EDABIT"
specifier = "odd"
print(get_elements(list_or_string,specifier))