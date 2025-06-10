from typing import Counter


def maxDifference(s: str) -> int:
    s_count = Counter(s)
    odd = []
    even = []
    for i in s_count.values():
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return max(odd)-min(even)

print(maxDifference("aaaaabbc"))
