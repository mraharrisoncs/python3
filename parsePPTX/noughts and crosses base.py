
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    
    # Add condition to return true if there is a match in the win conditions


def main():
    board = [[" ", " ", " "], [" ", " ", " "],[" ", " ", " "]]
    current_player = "X"
    move_count = 0

    while move_count < 9:
        print_board(board)
        row = int(input("Player " + current_player + ", enter the row (0-2): "))
        col = int(input("Player " + current_player + ", enter the col (0-2): "))


        # Complete condition to check if space chosen is blank
        if 
            # Add code to assign current player to the location
            
            
            move_count += 1
            if check_winner(board, current_player):
                print_board(board)
                print("Player "+ current_player + " wins!")
                return
            
            
            # Add the code to alternate players
            
            
        else:
            print("Cell already occupied, try again.")

    print_board(board)
    print("It's a draw!")

main()