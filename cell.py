X = "x"
E = " "

class Cell:
	def __init__(self, tile, color):
		self.tile = tile
		self.color = color

	def __repr__(self):
		return f"Cell([{self.tile}] {self.color})"

	def getTile(self):
		return self.tile

	def isEmpty(self):
		return self.tile == E
	
	def isFull(self):
		return self.tile == X
	
	@staticmethod
	def createFullCell(color):
		return Cell(X, color)

	@staticmethod
	def createEmptyCell(color):
		return Cell(E, color)
