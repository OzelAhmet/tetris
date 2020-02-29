import unittest
import blocks
from cell import X, E
from block import Block

class TestBlocks(unittest.TestCase):

    def setUp(self):
        self.T = Block([[E, X, E],
                        [X, X, X]],
                        "brown")

    def testInit(self):
        self.assertEqual("brown", self.T.block[0][0].color)
        self.assertEqual(2, self.T.height)
        self.assertEqual(3, self.T.width)


if __name__ == '__main__':
    unittest.main()