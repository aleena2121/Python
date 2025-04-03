def calculate_score(rolls):
    """
    This function calculates the score based on the die rolls given by the player

    Parameters
    ---
    rolls: a list of tuples containing each round of die rolls

    Returns:
    score: the total score of the player
    """
    score = 0
    for i in rolls:
        if i[0] == i[1]:
            return 0
        else:
            score += (i[0]+i[1])
    return score

rolls = []
for i in range(3):
    rolls.append(tuple(map(int,input(f"Enter number on dice on roll {i+1}: ").split())))
print(calculate_score(rolls))