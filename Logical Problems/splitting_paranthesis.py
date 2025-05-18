def split_parenthesis(parenthesis_string):
    """
    This function splits a parenthesis string into a list of balanced parenthesis clusters.

    Args:
    parenthesis_string: a string containing parentheses

    Returns:
    cluster: a list of balanced parenthesis strings
    """
    cluster = []
    curr = ""
    count = 0

    for char in parenthesis_string:
        curr += char
        if char == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            cluster.append(curr)
            curr = ""

    return cluster

print(split_parenthesis("()()()"))
