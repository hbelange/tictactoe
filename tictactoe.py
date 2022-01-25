
def start_game(board):
    start = input("Would you like to play Tic Tac Toe? (y/n) ")
    if start.lower() == "y":
        print_board(board)
    elif start.lower() == "n":
        print("Suit yourself")
    else:
        raise Exception("Answer must be one of the following: y/n")

def print_board(board):

    row_pointer = 0
    col_pointer = 0

    for row in range(13):
        if row % 4 == 0:
            print("-------------------------")
        elif (row+2) % 4 == 0:
            for col in range(25):
                if col % 8 == 0 and col != 24:
                    print("|", end="")
                elif col == 24:
                    print("|")
                elif col in [4, 12, 20]:
                    print(board[row_pointer][col_pointer], end="")
                    col_pointer += 1
                    if col_pointer == 3:
                        row_pointer += 1
                        col_pointer = 0
                else:
                    print(" ", end="")
                    
        else:
            for col in range(25):
                if col % 8 == 0 and col != 24:
                    print("|", end="")
                elif col == 24:
                    print("|")
                else:
                    print(" ", end="")

def player1(board):
    box = int(input("Player 1, choose a box from 1-9: "))
    if box < 1 or box > 9:
        print("Invalid Box")
        player1(board)
    elif box < 4:
        if board[0][box-1] != ' ':
            print("Choose an empty box.")
            player1(board)
        else:
            board[0][box-1] = "X"
    elif box < 7:
        if board[1][box-4] != ' ':
            print('Choose an empty box.')
            player1(board)
        else:
            board[1][box-4] = "X"
    elif box < 10:
        if board[2][box-7] != ' ':
            print('Choose an empty box.')
            player1(board)
        else:
            board[2][box-7] = "X"
    else:
        print("Invalid Box")
        player1(board)
    


def player2(board):
    box = int(input("Player 2, choose a box from 1-9: "))
    if box < 1 or box > 9:
        print("Invalid Box")
        player2(board)
    elif box < 4:
        if board[0][box-1] != ' ':
            print("Choose an empty box.")
            player2(board)
        else:
            board[0][box-1] = "O"
    elif box < 7:
        if board[1][box-4] != ' ':
            print('Choose an empty box.')
            player2(board)
        else:
            board[1][box-4] = "O"
    elif box < 10:
        if board[2][box-7] != ' ':
            print('Choose an empty box.')
            player2(board)
        else:
            board[2][box-7] = "O"
    else:
        print("Invalid Box")
        player2(board)

def isWon(board):
    #Check if row is filled with alike symbol
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][0] == board[row][2] and board[row][1] == board[row][2] and board[row][0] != ' ':
            return True
    #Check column
    for col in range(3):
        if board[0][col] == board[1][col] and board[0][col] == board[2][col] and board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    #Check diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    
    return False

def main(board):
    count = 0
    while isWon(board) == False and count < 9:
        if count % 2 == 0:
            player1(board)
        else:
            player2(board)
        print_board(board)
        isWon(board)
        count += 1
        if count == 9:
            print("Cat's Game")
    if count % 2 == 0:
        print("Player 2 Wins!")
    elif count % 2 != 0 and count != 9:
        print("Player 1 Wins!")

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
start_game(board)
main(board)


