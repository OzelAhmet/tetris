import random

from cell import Cell, X, E

class Block:
	def __init__(self, block, color=None):
		self.block = []
		for row in block:
			newRow = []
			self.block.append(newRow)
			for tile in row:
				if tile == X:
					newRow.append(Cell.createFullCell(color))
				else:
					newRow.append(Cell.createEmptyCell(color))

		self.height = len(block)
		self.width = len(block[0])

	def __repr__(self):
		return str(self.block)

	def __getitem__(self, item):
		"""
			'block[x, y]' can be used.
			[0, 0] is the top-left cell of the board.
		"""
		if item is not int and len(item) is 2:
			return self.block[item[1]][item[0]]
		else:
			return self.block[item]

	def isCellEmpty(self, x, y):
		return self[x, y].isEmpty()

	def isCellFull(self, x, y):
		return self[x, y].isFull()

	def getTransposedList(self):
		newBlock = [[None for _ in range(self.height)] for _ in range(self.width)]
		for y in range(self.height):
			for x in range(self.width):
				newBlock[x][self.height-1-y] = self[x, y]
		return newBlock

	def transposeBlock(self):
		newBlock = [[None for _ in range(self.height)] for _ in range(self.width)]
		for y in range(self.height):
			for x in range(self.width):
				newBlock[x][self.height-1-y] = self[x, y]
		
		self.block = newBlock
		self.width, self.height = self.height, self.width

	def transposeBlockBack(self):
		newBlock = [[None for _ in range(self.height)] for _ in range(self.width)]
		for y in range(self.height):
			for x in range(self.width):
				newBlock[self.width-1-x][y] = self[x, y]
		
		self.block = newBlock
		self.width, self.height = self.height, self.width


SQUARE = Block([[X, X], [X, X]], "white")
LINE = Block([[X, X, X, X]], "red")
"""
__|_0_1_2
0 | X X E
1 | E X X
"""

"""
__|_0_1
0 | E X
1 | X X
2 | X E
"""
Z = Block([[X, X, E], [E, X, X]], "blue")
Z_R = Block([[E, X, X], [X, X, E]], "green")
L = Block([[X, E, E], [X, X, X]], "orange")
L_R = Block([[E, E, X], [X, X, X]], "pink")
T = Block([[E, X, E], [X, X, X]], "brown")

blocks = [SQUARE, LINE, Z, Z_R, L, L_R, T]


def randomBlock():
	return random.choice(blocks)


if __name__ == "__main__":
	# getitem
	print(Z[2, 0])

	# isCell...
	print(LINE.isCellFull(0, 0))
	print(Z.isCellEmpty(2, 0))

	# transpose
	print("  0", Z)
	Z.transposeBlock()
	print(" 90", Z)
	Z.transposeBlock()
	print("180", Z)
	Z.transposeBlock()
	print("270", Z)
	Z.transposeBlock()
	print("  0", Z)

	#transposeBack
	print("   T", T)
	T.transposeBlock()
	print("  90", T)
	T.transposeBlockBack()
	T.transposeBlockBack()
	print(" -90", T)
