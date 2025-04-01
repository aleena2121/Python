def calculate_mini_wins(lottery):
    """
    This function returns the number of mini wins in the lottery ticket

    Parameters - 
    lottery: a list of lists contianing a string and a number

    Returns -
    The total count of mini wins in the lottery ticket
    """
    mini_wins = 0
    for i in lottery:
        if chr(int(i[1])) in i[0]:
            mini_wins += 1
    return mini_wins

lottery = []
num_of_strings = int(input("Enter the number of strings in the ticket: "))
for i in range(num_of_strings):
    sublist = []
    string = input(f"Enter string {i+1}: ")
    sublist.append(string)
    number = input(f"Enter number {i+1}: ")
    sublist.append(number)
    lottery.append(sublist)
win = int(input("Enter number of wins: "))
no_of_mini_wins = calculate_mini_wins(lottery)
if no_of_mini_wins >= win:
    print("Winner!")
else:
    print("Loser!")