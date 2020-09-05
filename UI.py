from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM, ALL

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

class SudokuUI(Frame):
    """
    The Tkinter UI, responsible for drawing the board and accepting user input.
    """
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
        # random_button = Button(self,
        #                       text="New Puzzle",
        #                       command=self.__new_puzzle)
        # random_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()

        # self.canvas.bind("<Button-1>", self.__cell_clicked)
     
    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
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
                    # self.canvas.delete()
                    self.canvas.create_text(
                        x, y, text="", tags="numbers", fill=color)


    def uupdate(self, root, game, i, j):
        
        self.game = game
        self.__draw_puzzle()