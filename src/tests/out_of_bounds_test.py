import sys, unittest
from ..Game import next_position
from ..Board import initialise_board

class TestBoard(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_outOfBounds(self):
        board = initialise_board(4,4)
        self.assertEqual(next_position((3,3),'R', board), (3,0))
 
if __name__ == '__main__':
    unittest.main()