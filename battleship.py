from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)
def print_board(board):
    ocean = []
    for row in board:
        ships = " ".join(row)
        ocean.append(ships)
    for i in ocean:
        print "\t",i
    print "\n"
print "\n***Let's play Battleship!***\n"
print_board(board)
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(5):
    print "%s out of 5 chances...\n" %(turn+1)
    guess_row = int(raw_input("Guess Row (Starts with '0'): "))
    guess_col = int(raw_input("Guess Column (Starts with '0'): "))

    if guess_row == ship_row and guess_col == ship_col:
        print "#"*35
        print "\n***Congratulations! You sunk my battleship!***\n"
        print "#"*35
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "\n***Oops, that's not even in the ocean.***"
        elif(board[guess_row][guess_col] == "X"):
            print "\n***You guessed that one already.***"
        else:
            print "\n ***You missed the battleship!***"
            board[guess_row][guess_col] = "X"
    print 
    print_board(board)
    if turn == 4:
        print "\t***Game Over***\n"