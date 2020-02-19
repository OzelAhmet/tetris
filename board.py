import blocks
import cell
import copy


class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "(x:{0} y:{1})".format(self.x, self.y)

	def getRight(self):
		return Pos(self.x + 1, self.y)

	def getLeft(self):
		return Pos(self.x - 1, self.y)

	def getBottom(self):
		return Pos(self.x, self.y + 1)

	def getRelativePos(self, x, y):
		return Pos((self.x + x), (self.y + y))


Pos = Position


class Board(blocks.Block):
	def __init__(self, width, height):
		mainBoard = [[blocks.E for _ in range(width)] for _ in range(height)]
		super().__init__(mainBoard)
		self.board = self.block  # alias

	def __str__(self):
		return "\n".join(map(lambda row : "".join(map(cell.Cell.getTile, row)), self.board)).replace(" ", "_")

	def isThereCollision(self, block, position):
		try:
			for y in range(block.height):
				for x in range(block.width):
					if (position.x < 0) or (block.isCellFull(x, y) and self.isCellFull((x + position.x), (y + position.y))):
						return True
		except IndexError:  # bottom or right
			return True
		return False

	def putNewBlock(self, block, position):
		for y in range(block.height):
			for x in range(block.width):
				if block.isCellFull(x, y):
					self.board[y + position.y][x + position.x] = block[x, y]

	def getCopyOfBoard(self):
		return copy.deepcopy(self.board)


class BlockBoard(Board):
	def __init__(self, width, height):
		super().__init__(width, height)
		self.activeBlock = None
		self.blockPosition = None
		self.removedLineCount = 0

	def setBlock(self, block):
		self.activeBlock = block
		self.blockPosition = Pos(self.width // 2, 0)
		if self.isThereCollision(self.activeBlock, self.blockPosition):
			return False
		return True

	# TODO: change later
	def getCurrentBoard(self):
		currentBoard = self.getCopyOfBoard()
		for y in range(self.activeBlock.height):
			for x in range(self.activeBlock.width):
				if self.activeBlock.isCellFull(x, y):
					currentBoard[y + self.blockPosition.y][x + self.blockPosition.x] = self.activeBlock[x, y]
		return currentBoard

	def clearFullLines(self):
		fullLine = [blocks.X for _ in range(self.width)]
		emptyLine = [blocks.E for _ in range(self.width)]
		while True:
			try:
				self.board.remove(copy.deepcopy(fullLine))
				self.removedLineCount += 1
				self.board.insert(0, copy.deepcopy(emptyLine))
			except ValueError:
				break

	def saveBlock(self):
		self.putNewBlock(self.activeBlock, self.blockPosition)
		self.clearFullLines()

	def shiftBlockRight(self):
		if not self.isThereCollision(self.activeBlock, self.blockPosition.getRight()):
			self.blockPosition = self.blockPosition.getRight()
			return True
		return False

	def shiftBlockLeft(self):
		if not self.isThereCollision(self.activeBlock, self.blockPosition.getLeft()):
			self.blockPosition = self.blockPosition.getLeft()
			return True
		return False

	def shiftBlockBottom(self):
		if not self.isThereCollision(self.activeBlock, self.blockPosition.getBottom()):
			self.blockPosition = self.blockPosition.getBottom()
			return True
		return False

	def transposeBlock(self):
		"""
		top-left is the center of rotation
		"""
		self.activeBlock.getTranspose()
		if self.isThereCollision(self.activeBlock, self.blockPosition):
			self.activeBlock.transposeBlockBack()


if __name__ == "__main__":
	# Pos
	p = Pos(1, 1)
	print(
		p.getRight(),
		p.getLeft(),
		p.getBottom()
	)

	# Board
	board = Board(10, 16)

	print(
		board.isThereCollision(blocks.SQUARE, Pos(0, 14)),
		board.isThereCollision(blocks.SQUARE, Pos(0, 15)),
		board.isThereCollision(blocks.LINE, Pos(0, 15))
	)

	print("old\n", board)
	board.putNewBlock(blocks.LINE, Pos(5, 15))
	print("new\n", board)

	# BlockBoard
	board = BlockBoard(10, 16)
	board.board[-1] = [blocks.X for _ in range(board.width)]
	board.clearFullLines()
	print(board.removedLineCount)
	print(board)
