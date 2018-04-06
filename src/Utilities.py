import sys

def read_coordinate(position):
  position = position.replace('(','')
  position = position.replace(')','')
  coord = [ int(val) for val in position.split(',')]
  return (coord[0],coord[1])
  

def read_input(file_name):

  descriptions = []
  file = open(file_name, 'r')

  # clean content
  lines = file.readlines()
  for i in range(len(lines)):
    descriptions.append(lines[i].strip('\n').strip())

  # read dimension
  gridsize = int(descriptions[0])

  # read zombie.
  zombie = read_coordinate(descriptions[1])

  # position of creatures.
  creatures = []
  for coord in descriptions[2].split(" "):
    creatures.append(read_coordinate(coord))

  # zombie moves.
  directions = []
  for direction in list(descriptions[3]):
    directions.append(direction)

  # cleanup
  file.close()

  return gridsize, zombie, creatures, directions



class Outputter:

  score = 0
  positions = []
  SCORE_MESSAGE = "zombies score: "
  POSITION_MESSAGE = "zombies positions: \n"

  def __init__(self,score,positions):
    self.score = str(score)
    self.positions = positions

  def console(self):
    formatted = self.format_positions(self.positions)
    print self.SCORE_MESSAGE, self.score
    print self.POSITION_MESSAGE, formatted

  def text_file(self,file_name):
    file = open(file_name, 'w')
    formatted = self.format_positions(self.positions)
    file.write(self.SCORE_MESSAGE + self.score + "\n")
    file.write(self.POSITION_MESSAGE + formatted + "\n")

    file.close()
    return

  def format_positions(self,positions):
    formatted = ""
    for position in positions:
       formatted += "({0},{1})".format(position[0],position[1])
    return  formatted
