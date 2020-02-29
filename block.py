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
			x: horizantal, y: vertival
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