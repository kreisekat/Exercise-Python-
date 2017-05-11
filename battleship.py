"""Battleship game, as practiced on codecademy, but in python 3. A random boat
is generated and the user has 4 attempts to guess where it is. """

#import random function
from random import randint

#empty list
board = []
#creating a 5 x 5 board filled with "O"s
for x in range(5):
    board.append(["O"] * 5)
#function to print out the board
def print_board(board):
    for row in board:
        grid = " ".join(row)
        print(grid)

print("Let's play Battleship!")
print_board(board)
#generates random row and column
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col

#gives the player 4 attempts to guess the right row and column
for turn in range(4):
    guess_row = int(input("Guess row:"))-1
    guess_col = int(input("Guess column:"))-1
#win situation
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
#guessed wrong
    else:
        #wrong guess, because out of range
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        #wrong guess, because this was already guessed and wrong
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        #wrong guess
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        #out of guesses
        if turn == 3:
            print("Game Over")
            break
        #shows current turn
        print("Turn", turn + 1)
        print_board(board)
