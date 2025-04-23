def count_missing_numbers(nums):
    """
    Function to count the number of missing numbers

    Args: 
    nums: a list of numbers and strings

    Returns:
    count: count of missing numbers
    """
    cleaned = [int(x) for x in nums if x.isdigit()]
    count = 0
    for num in range(min(cleaned),max(cleaned)):
        if num not in cleaned:
            count += 1
    return count

print(count_missing_numbers(["1", "3", "A", "7", "9"]))