import math
from random import randrange

def convert_space_to_row_col(space):
    return ((space - 1) // 3, (space - 1) % 3)
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    row_separator = "+-------+-------+-------+"
    empty_line = "|       |       |       |"

    print(row_separator)
    for row in board:
        print(empty_line)
        print("|   " + "   |   ".join(str(cell) for cell in row) + "   |")
        print(empty_line)
        print(row_separator)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    free_fields = make_list_of_free_fields(board)
    while True:
        try:
            user_move = int(input("Enter your move: "))
            if 1 <= user_move <= 9:
                (row,col)  = convert_space_to_row_col(user_move)
                if (row,col) in free_fields:
                    board[row][col] = "O"
                    break
                else:
                    print("That space has already been picked - choose a different space")
            else:
                print("You must choose a space between 1 and 9")
        except ValueError:
            print("Please enter a number.")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return [
        (i,j)
        for i, row in enumerate(board)
        for j, cell in enumerate(row)
        if isinstance(cell,int)
    ]
    

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    for row in board:
        if all(cell == sign for cell in row):
            return sign

    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return sign
                    
    if all(board[i][i] == sign for i in range(3)):
        return sign
    if all(board[i][2 - i] == sign for i in range(3)):
        return sign
    
    return None

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    while True:
        computer_move = randrange(9) + 1
        (row,col)  = convert_space_to_row_col(computer_move)
        if (row,col) in free_fields:
            board[row][col] = "X"
            print("Computer chooses space #", computer_move)
            break

def play_game():
    board = [[(3*n)+1, (3*n)+2, (3*n)+3] for n in range(3)]
    board[1][1] = "X"

    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, "O") == "O":
            print("Game Over, You Win!")
            return
        draw_move(board)
        display_board(board)
        if victory_for(board,"X") == "X":
            print("Game Over, Computer Wins!")
            return
        if make_list_of_free_fields(board) == []:
            print("Game Over, you tied.")
            return
    


def main():
    while True:
        play_game()
        while True:
            play_again = input("Do you want to play again? (Y or N): ").strip().upper()
            if play_again == "N":
                return  # exit the main loop
            elif play_again == "Y":
                break   # break out of inner loop and replay
            else:
                print("Invalid input, try again.")

main()