import sys
from Board import *
from Game import *
from Utilities import *


if __name__== "__main__":

  positions = []
  
  
  # Read File
  gridsize, zombie, creatures, directions = read_input('./config/input.txt')

  # Prepare Board
  board = initialise_board(gridsize,gridsize)
  load_board(board,zombie,creatures)

  # Load first Zombie
  new_zombie(zombie)

  # Moves Zombies
  for zombie in zombies:
    print "new zombie is on the move!"
    last_position = moves_logic(board, directions, zombie)
    positions.append(last_position) 
    print last_position
  # Used Single-responsibility Principle SOLID
  output = Outputter(len(positions)-1, positions)
  output.console()
  output.text_file('output.txt')
  