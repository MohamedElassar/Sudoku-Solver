from tkinter import *
import time

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

#Class to create UI using tkinter library
class SudokuUI(Frame):
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)
        self.row, self.col = 0, 0
        self.__initUI()

    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        self.__draw_grid()
        self.__draw_puzzle()

#Method to draw grid for puzzle
    def __draw_grid(self):
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"
            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

#Method to draw intial puzzle 
    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.puzzle[i][j]
                x = MARGIN + j * SIDE + SIDE / 2
                y = MARGIN + i * SIDE + SIDE / 2
                color = "black"
                if answer != 0: 
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color)
                else:
                    pass

#Method to update the puzzle every time a possible solution is
#guessed or to clear incorrect solution
    def update(self, root, game, i, j):
        self.game = game
        answer = self.game.puzzle[i][j]
        x = MARGIN + j * SIDE + SIDE / 2
        y = MARGIN + i * SIDE + SIDE / 2
        color = "red"
        if answer != 0: 
            self.canvas.create_text(
                x, y, text=answer, tags="hello" + str(9*i+j), fill=color)
        else:
            self.canvas.delete("hello" + str(9*i+j))

        root.update()
        time.sleep(0.1)