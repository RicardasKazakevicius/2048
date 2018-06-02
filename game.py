from Tkinter import *
from grid_numbers import *

GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = { 2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
													32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
													512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }
CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
										32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
										512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2" }
FONT = ("Verdana", 40, "bold")

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"

class Game(Frame):
	def __init__(self, y_size, x_size):
		Frame.__init__(self)

		self.y_size = y_size
		self.x_size = x_size

		self.grid()
		self.master.title('2048')
		self.master.bind("<Key>", self.key_pressed)

		self.grid_numbers = GridNumbers(y_size, x_size)
		self.grid_numbers.create_number()

		self.grid_cells = []
		self.init_grid()
		self.update_grid_cells()
		
		self.mainloop()

	def init_grid(self):
		background = Frame(self, bg=BACKGROUND_COLOR_GAME)
		background.grid()
		for i in range(self.y_size):
			grid_row = []
			for j in range(self.x_size):
				cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY)
				cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
				t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)
				t.grid()
				grid_row.append(t)
			self.grid_cells.append(grid_row)

	def update_grid_cells(self):
		for i in range(self.y_size):
			for j in range(self.x_size):
				if self.grid_numbers.get_numbers()[i][j] == 0:
					self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
				else:
					self.grid_cells[i][j].configure(text=str(self.grid_numbers.get_numbers()[i][j]), bg=BACKGROUND_COLOR_DICT[self.grid_numbers.get_numbers()[i][j]], fg=CELL_COLOR_DICT[self.grid_numbers.get_numbers()[i][j]])
		if self.grid_numbers.is_dead_end():
			print ''
		self.update_idletasks()

	def key_pressed(self, event):
		numbers = self.grid_numbers.get_numbers().copy()
		key = repr(event.char)
		if key == KEY_RIGHT:
			self.grid_numbers.right()
		elif key == KEY_LEFT:
			self.grid_numbers.left()
		elif key == KEY_UP:
			self.grid_numbers.up()
		elif key == KEY_DOWN:
			self.grid_numbers.down()
		else:
			return 
		if self.grid_numbers.is_free_cell():
			self.grid_numbers.create_number()
		self.update_grid_cells()

		
		