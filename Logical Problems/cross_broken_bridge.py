from collections import Counter

def can_patch(bridge,planks):
    """
    Function to tell if a person can cross the broken bridge with given planks or not

    Args:
    bridge: a list representating bridge
    planks: a list of sizes of planks available

    Returns:
    True if bridge can be crossed, else false
    """
    plank_counts = Counter(planks)
    no_of_holes = 0
    i = 0
    while i < len(bridge):
        if bridge[i] == 0:
            no_of_holes += 1
        else:
            if no_of_holes > 1:
                if plank_counts[no_of_holes] > 0:
                    plank_counts[no_of_holes] -= 1
                else:
                    return False
            no_of_holes = 0
        i += 1

    if no_of_holes > 1:  # if bridge ends with holes
        if plank_counts[no_of_holes] > 0:
            plank_counts[no_of_holes] -= 1
        else:
            return False

    return True


print(can_patch([1, 0, 0, 0, 0, 0, 0, 1], [4, 1, 2, 3, 4]))