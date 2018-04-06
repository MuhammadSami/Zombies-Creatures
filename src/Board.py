
# the reason i made it row and col was
# that it was modifiable in the feature. 
# product owner might say we want to make it longer and thinner.
def initialise_board(row,col):
    board = [[" "]*col for unused in range(row)]
    return board


def load_board(board,zombie,creatures):
    board[zombie[0]][zombie[1]] = 'Z'
    for creature in creatures:
        board[creature[0]][creature[1]] = 'C'

def display_board(board):
     for items in board:
        print items