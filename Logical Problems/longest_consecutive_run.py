def longest_run(arr):
    """
    This function returns the length of the longest consecutive run

    Args:
    arr : a list of numbers

    Returns: 
    max_len : length of longest consecutive run
    """
    if not arr:
        return 0

    max_len = 1
    inc_len = 1
    dec_len = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1: 
            inc_len += 1
            dec_len = 1
        elif arr[i] == arr[i - 1] - 1: 
            dec_len += 1
            inc_len = 1
        else:
            inc_len = 1
            dec_len = 1
        max_len = max(max_len, inc_len, dec_len)

    return max_len

print(longest_run([1, 2, 3, 5, 6, 7, 8, 9]) )