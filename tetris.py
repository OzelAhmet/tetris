# 05-01-2020

import curses
import time

from board import BlockBoard
import blocks

WAIT_TIME = 1
H = 16
W = 10


def print_board(board: list):
	for row in range(len(board)):
		row_str = "|"
		row_str += " ".join(board[row])
		row_str += "|"
		stdscr.addstr(row, 0, row_str)
	stdscr.refresh()


def print_log(row, log):
	stdscr.clrtoeol()
	stdscr.addstr(row + H + 2, 0, str(log))
	stdscr.refresh()


def shiftBlock(key, board: BlockBoard):
	if key == curses.KEY_LEFT:
		board.shiftBlockLeft()
	elif key == curses.KEY_RIGHT:
		board.shiftBlockRight()
	elif key == curses.KEY_DOWN:
		board.shiftBlockBottom()
	elif key == curses.KEY_UP:
		board.transposeBlock()

	tempBoard2 = board.getCurrentBoard()
	print_board(tempBoard2)


if __name__ == "__main__":
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)
	# stdscr.nodelay(True)
	stdscr.timeout(WAIT_TIME * 1000)

	mainBoard = BlockBoard(W, H)
	print_board(mainBoard.board)
	print_log(0, "Score: {0}".format(mainBoard.removedLineCount))

	try:
		while True:
			newBlockSuccessful = mainBoard.setBlock(blocks.randomBlock())

			if not newBlockSuccessful:  # end game
				break

			while True:
				print_board(mainBoard.getCurrentBoard())

				endWait = time.time() + WAIT_TIME
				while time.time() < endWait:
					pressedKey = stdscr.getch()
					shiftBlock(pressedKey, mainBoard)

				# shift block bottom
				shiftBottomSuccessful = mainBoard.shiftBlockBottom()
				if not shiftBottomSuccessful:
					break

			# there is collusion, update board
			mainBoard.saveBlock()
			print_log(0, "Score: {0}".format(mainBoard.removedLineCount))

	except KeyboardInterrupt:
		print("quit")
	finally:
		curses.echo()
		curses.nocbreak()
		stdscr.keypad(False)
		curses.endwin()
		print("Game Over")
		print("Score: {0}".format(mainBoard.removedLineCount))
