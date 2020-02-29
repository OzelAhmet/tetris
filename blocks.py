import random
from cell import X, E
from block import Block

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
