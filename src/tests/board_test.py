import sys, unittest
from ..Board import initialise_board

class TestBoard(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_grid(self):
        board = initialise_board(4,4) 
        self.assertEqual(len(board), 4)
 
if __name__ == '__main__':
    unittest.main()