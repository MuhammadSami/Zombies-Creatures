from Board import display_board

zombie_score = 0
zombies = []
def moves_logic(board, moves, zombie):
    directions = list(moves)
    curr_pos = zombie

    for direction in directions:
        display_board(board)
        new_pos = next_position(curr_pos, direction, board)
        current = board[curr_pos[0]][curr_pos[1]]
        piece = board[new_pos[0]][new_pos[1]]
        if (current != "Z"):
            board[curr_pos[0]][curr_pos[1]] = ' '
            
        if piece  == "C":
            new_zombie(new_pos)
            update_score()
            board[new_pos[0]][new_pos[1]] = 'Z'
        curr_pos = new_pos
    return curr_pos
    
def next_position(curr_zombie, direction, board):
    print "Current Zombie: ",curr_zombie
    if direction == "L":
        xy = ((curr_zombie[0]) % len(board), (curr_zombie[1]-1) % len(board))
        return xy
    if direction == "R":
        xy = ((curr_zombie[0]) % len(board), (curr_zombie[1]+1) % len(board))
        return xy
    if direction == "U":
        xy = ((curr_zombie[0]-1) % len(board), curr_zombie[1] % len(board))
        return xy
    if direction == "D":
        xy = ((curr_zombie[0]+1) % len(board), curr_zombie[1] % len(board))
        return xy


def new_zombie(zombie):
    zombies.append(zombie)
    return zombies

def update_score():
    global zombie_score
    zombie_score += 1

