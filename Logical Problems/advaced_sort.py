def advanced_sort(items):
    """
    Function that returns a list with the items from the original list stored into sublists

    Args: 
    items: a list given by user

    Returns:
    result: list sorted into sublists
    """
    seen = []
    result = []
    for item in items:
        if item not in seen:
            seen.append(item)
            result.append([item]*items.count(item))
    return result

print(advanced_sort(["b", "a", "b", "a", "c"]))
