import random

X = "x"
E = " "


class Block:
	def __init__(self, block):
		self.block = block
		self.height = len(block)
		self.width = len(block[0])

	def __getitem__(self, item):
		if item is not int and len(item) is 2:
			# x, y  # 0, 0 is top-left
			return self.block[item[1]][item[0]]
		else:
			return self.block[item]

	def isCellEmpty(self, x, y):
		return self[x, y] == E

	def isCellFull(self, x, y):
		return self[x, y] == X

	def getTranspose(self):
		newBlock = [[None for _ in range(self.height)] for _ in range(self.width)]
		for y in range(self.height):
			for x in range(self.width):
				newBlock[x][self.height-1-y] = self[x, y]
		return newBlock


SQUARE = Block([[X, X], [X, X]])
LINE = Block([[X, X, X, X]])
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
Z = Block([[X, X, E], [E, X, X]])
Z_R = Block([[E, X, X], [X, X, E]])
L = Block([[X, E, E], [X, X, X]])
L_R = Block([[E, E, X], [X, X, X]])
T = Block([[E, X, E], [X, X, X]])

blocks = [SQUARE, LINE, Z, Z_R, L, L_R, T]


def randomBlock():
	return random.choice(blocks)


if __name__ == "__main__":
	print(Z[2, 0])

	print(LINE.isCellFull(0, 0))
	print(Z.isCellEmpty(2, 0))

	print(Z.block)
	Z = Block(Z.getTranspose())
	print(Z.block)
	Z = Block(Z.getTranspose())
	print(Z.block)
	Z = Block(Z.getTranspose())
	print(Z.block)
	Z = Block(Z.getTranspose())
	print(Z.block)
