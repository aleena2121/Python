import random

def coin_flip(n):
    """
    Generates random number to count the number of heads or tails and get percentage

    Parameters:
    n : a integer denoting the number of flips

    Returns :
    Percentage of heads and tails
    """
    head = 0
    tail = 0
    for i in range(n):
        x = random.random()

        if x<0.5:
            tail += 1
        else:
            head += 1
    
    return ((head/n)*100,(tail/n)*100)


n = int(input())
if n<1:
    print("Invalid input")
else:
    head_percentage,tail_percentage = coin_flip(n)
    print(head_percentage,tail_percentage)