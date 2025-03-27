import random
def gamble(stake,goal):
    """
    This function gives the average number of wins and average win and loss percentage for a gambling experiment

    Parameters:
    stake: an integer denoting the starting amount
    goal: an integer denoting the end goal
    n: the number of times the experiment should run

    Returns:
    checks if the gambler wins or not and return the number of bets
    """
    s = stake
    bets = 0
    while s != 0 and s != goal:
        bets += 1
        x = random.random()
        if x < 0.5:
            s -= 1
        else:
            s += 1
    
    if s == goal:
        return(bets,1)
    else:
        return(bets,0)
    


stake = int(input())
goal = int(input())
number_of_simulations = int(input())
number_of_wins = 0
number_of_bets = [0]*number_of_simulations
for i in range(number_of_simulations):
    number_of_bets[i],result = gamble(stake,goal)
    number_of_wins += result
print(number_of_bets)
print("Average number of bets: " + str(sum(number_of_bets)/number_of_simulations))
print("Number of wins: "+ str(number_of_wins))
print("Percentage of wins: "+ str((number_of_wins/number_of_simulations)*100))
print("Percentage of loss: "+ str(((number_of_simulations-number_of_wins)/number_of_simulations)*100))