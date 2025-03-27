import random

def print_board(board):
    """
    Prints the Tic-Tac-Toe Board

    Parameters:
    board: A 2D array representating the current state of the board

    Returns:
    Prints the current state of the board
    """
    for row in board:
        print(" ".join(row))
    print("\n")

def check(board):
    """
    Checks the state of the match, i.e., User wins, Computer Wins or Draw

    Parameters:
    board: A 2D array representating the current state of the board

    Returns:
    Returns if the game has ended or not and if ended, prints the winner

    """
    cell = 0
    for i in range(3):
        cell += board[i].count("-")
    if cell == 0:
        print("It's a Draw!")
        return True
    else:
        for i in range(0,3):
            if (board[i][0] == board[i][1] == board[i][2] == "O") or (board[i][0] == board[i][1] == board[i][2] == "X"):
                if (board[i][0]) == "X":
                    print("You have won!")
                else:
                    print("Computer has won")
                return True
        for i in range(0,3):
            if (board[0][i] == board[1][i] == board[2][i] == "O") or (board[0][i] == board[1][i] == board[2][i] == "X"):
                if (board[0][i]) == "X":
                    print("You have won!")
                else:
                    print("Computer has won")
                return True 
        if (board[0][0] == board[1][1] == board[2][2] == "O") or (board[0][0] == board[1][1] == board[2][2] == "X"):
            if (board[0][0]) == "X":
                    print("You have won!")
            else:
                print("Computer has won")
            return True
        if (board[0][2] == board[1][1] == board[2][0] == "O") or (board[0][2] == board[1][1] == board[2][0] == "X"):
            if (board[0][2]) == "X":
                    print("You have won!")
            else:
                print("Computer has won")
            return True
        else:
            return False

def user_input(board):
    """
    Takes user input

    Parameters:
    board: A 2D array representating the current state of the board

    Returns:
    Prints the current state of the board
    """
    while True:
        row = int(input("Enter row (0-2): "))
        column = int(input("Enter column (0-2): "))
        if 0 <= row < 3 and 0 <= column < 3:
            if board[row][column] == "-":
                board[row][column] = "X"
                print("Your turn")
                print_board(board)
                return check(board)
            else:
                print("Cell already filled! Enter a new row and column:")
        else:
            print("Enter valid numbers!")

def computer_input(board):
    """
    Takes random computer input

    Parameters:
    board: A 2D array representating the current state of the board

    Returns:
    Prints the current state of the board
    """
    while True:
        row = random.choice([0,1,2])
        column = random.choice([0,1,2])
        if board[row][column] == '-':
            board[row][column] = "O"
            print("Computer's Turn")
            print_board(board)
            return check(board)


board = [["-" for _ in range(3)] for _ in range(3)]
print_board(board)
user_result = False
computer_result = False

while not user_result and not computer_result:
    user_result = user_input(board)
    if user_result == False:
        computer_result = computer_input(board)