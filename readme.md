# Zombies and Creatures

This game reads an input file with commands about the size of grid, starting position of a Zombie, location of all the creatures and the directions the zombie will move. As soon as the zombie is in the same cell as a Creature it turns into a zombie and once the first zombie is done moving the second zombie starts moving using the same directions as the previous one.

## Getting Started

To start modify the input.txt file by adding Grid size, Location of one Zombie, Location of creatures and the directions of the zombie e.g

	
	5
	(2,1)
	(0,1) (1,2) (3,1) (0,4)
	DLUURRL

###### *Please make sure there is a space between all the creatures coordinates

To run the program open the terminal in the directory of the project.<br/>
 `Python Main.py`


### Prerequisites

The program is written using `python 2.7.12`, please make sure you have the right version before running the program.

Download python from [Python.org](https://www.python.org/)

Here is a guide on installing python on different Operating systems 
[Guide to Install Python](http://docs.python-guide.org/en/latest/starting/installation/)

### Directory Structure
#### Main.py

- Contains the main where all the functions for the game loop are being called.

#### Utilities.py

- Contains the logic to read the file and sanitize the input
- read_input(file)
	- reads the file and initializes all the variables
- read_coordinates(position) reads the coordinate 
	- Reads the coordinates and adds them as Tuples 
- Class Outputter to write a text output file with scores
	- Formats the text, Writes text to file, Closes the file
#### Game.py
- Contains the logic for moves to change directions of the zombies, add new zombies and update score. 
-  moves_logic(board, moves, zombie) 
	- Contains logic to move the zombie and replace pieces on the board
-  next_position(curr_zombie, direction, board)
	- returns all the possible moves for the Zombie
-  new_zombie(zombie)
	-  Adds new zombie into an array of zombies
-  update_score()
	-  updates the score for the Zombies
#### Board.py 
Generates the board and initializes the board with all the initial positions from the input file.

- initialise_board(row,col)
	- Creates the board with variable rows and columns
- load_board(board,zombie,creatures)
	- Loading all the pieces onto the board
- display_board(board)
	- Displays the board.

## Testing

- Board_test.py
	- Testing the length of the board
- From the Directory Zombies and Structure 
- Running the test: ` python src.tests.board_test `
## Versioning
V 1.0.0 

## Backlog
* add a build pipeline
* create more units tests

## Authors

Muhammad Sami-Ur-Rehman (m.samidevs@gmail.com)