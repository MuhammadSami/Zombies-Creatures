import sys, unittest, os
from ..Utilities import read_input
from ..Utilities import Outputter

class TestBoard(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_read(self):
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'input_test.txt')
        self.assertEqual(read_input(my_file),(5, (2,1), [(0,1),(1,2),(3,1)], ['D','L','U','U','R','R']))
    
    def test_output(self):
        output = Outputter(3, [(0,1),(1,2),(3,1)])
        output.text_file('output_test.txt')
        this_folder = os.getcwd()
        my_file = os.path.join(this_folder, 'output_test.txt')
        readfile = open(my_file,'r')
        if not my_file:
            return False
        else:
            self.assertEqual(readfile.readlines(),['zombies score: 3\n', 'zombies positions: \n', '(0,1)(1,2)(3,1)\n'])

if __name__ == '__main__':
    unittest.main()