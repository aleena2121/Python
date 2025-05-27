def merge(intervals):
    """
    This function merges all overlapping intervals and return an array of 
    the non-overlapping intervals that cover all the intervals in the input.

    Args: 
    intervals: a list of list of integers

    Returns:
    result: a list of merge intervals
    """
    intervals = sorted(intervals, key = lambda x:x[0])
    result = []
    for i in intervals:
        if not result or result[-1][1] < i[0]:
            result.append(i)
        else:
            result[-1][1] = max(result[-1][1],i[1])
    return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))