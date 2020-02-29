import unittest
from cell import Cell, X, E

class TestCell(unittest.TestCase):

    def setUp(self):
        self.cell = Cell("tile", "color")
        self.emptyCell = Cell.createEmptyCell("emptyColor")
        self.fullCell = Cell.createFullCell("fullColor")

    def testInit(self):
        self.assertEqual("tile", self.cell.tile)
        self.assertEqual("color", self.cell.color)

    def testRepr(self):
        self.assertEqual("Cell([tile] color)", str(self.cell))

    def testGetTile(self):
        self.assertEqual("tile", self.cell.getTile())

    def testCreateFullCell(self):
        self.assertEqual(X , self.fullCell.tile)

    def testCreateEmptyCell(self):
        self.assertEqual(E, self.emptyCell.tile)

    def testIsEmpty(self):
        self.assertEqual(True, self.emptyCell.isEmpty())
        self.assertEqual(False, self.fullCell.isEmpty())

    def testIsFull(self):
        self.assertEqual(True, self.fullCell.isFull())
        self.assertEqual(False, self.emptyCell.isFull())


if __name__ == '__main__':
    unittest.main()