import string
import Puzzles
import random
import UI
import time
import tkinter
from tkinter import *

ROWS = 9
COLS = 9

class Board(object):
	#Method to generate a random puzzle from the file "Puzzles.py"
	def __init__(self):
		r = str(random.randint(1, len(Puzzles.Puzzle)))
		self.puzzle = Puzzles.Puzzle[r]
		self.dividedPuzzle(self.puzzle)

	#Method to divide the sudoko grid into 9
	#each square is an element in a dictionary called "dividedGrid"
	def dividedPuzzle(self, puzzle):
		x = {}
		temp = []
		ctr = 0

		for m in range(0,9,3):
			for k in range(0,9,3):
				for i in range(3):
					for j in range(3):
						temp.append(puzzle[i + m][j + k])
				x[str(ctr)] = temp
				ctr +=1
				temp = []

		self.dividedGrid = x

	
	def updateDividedPuzzle(self, num, grid):

		self.dividedGrid[str(grid)].append(num)
	

	def undoUpdateDividedPuzzle(self, grid):
		
		self.dividedGrid[str(grid)].remove(self.dividedGrid[str(grid)][-1])

##############################################
#Method for printing the grid in the terminal
def printGrid(grid):
	for i in grid:
		print(i)
	print("***************************************")

##############################################
#Method to check if the guess made is a viable entry in its row and column
#Checks if the same value exists along the same row, column, and grid
def isPossibleSol(num, row, col, board):
	
	for j in range(COLS):
		if(board.puzzle[row][j] == num and j != col):
			return False
	for j in range(ROWS):
		if(board.puzzle[j][col] == num and j != row):
			return False

	grid = whichGrid(col, row)

	if(num in board.dividedGrid[str(grid)]):
		return False

	board.updateDividedPuzzle(num, grid)

	return True


def whichGrid(col, row):

	x = col // 3
	y = row // 3
	grid = y*3 + x
	return grid	
	
##############################################
#Recursive, back-tracking function to solve the puzzle
#When it finds a possible solution, the funtion stops and 
#calls itself, trying to continue solving the puzzle based on that new entry
def solve(board, UI, root):
	for i in range(ROWS):
		for j in range(COLS):
			if(board.puzzle[i][j] == 0):
				for guess in range(1,10):
					if(isPossibleSol(guess, i, j, board)):
						board.puzzle[i][j] = guess
						UI.update(root, board, i, j)
						if(solve(board, UI, root)):
							board.puzzle[i][j] = 0
							UI.update(root, board, i, j)
							board.undoUpdateDividedPuzzle(whichGrid(j, i))
						else:
							return 0
				return 1
	printGrid(board.puzzle)
	time.sleep(3)
	return 0


new_board = Board()
root = Tk()

gui = UI.SudokuUI(root, new_board)
root.update()
time.sleep(1)

solve(new_board, gui, root)
