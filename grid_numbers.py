import random
import numpy as np

class GridNumbers:
	def __init__(self, y_size, x_size):
		self.y_size = y_size
		self.x_size = x_size
		self.numbers = np.zeros((y_size, x_size)).astype(int)
		self.score = 0

	# create new number in free position
	def create_number(self):
		y_axis, x_axis = self.__get_random_postition()
		while self.is_used(y_axis, x_axis):
			y_axis, x_axis = self.__get_random_postition()
		self.numbers[y_axis, x_axis] = self.__get_random_number()

	# check if position is already used
	def is_used(self, y_axis, x_axis):
		return self.numbers[y_axis, x_axis] 

	# generate position randomly 
	def __get_random_postition(self):
		return random.randrange(self.y_size), random.randrange(self.x_size)

	# generate randomly number 2 with 80% chance or 4 with 20% chance
	def __get_random_number(self):
		random_number = random.randint(1, 5)
		if random_number > 1:
			return 2
		else:
			return 4

	def right(self):
		self.past_numbers = self.numbers.copy()
		for y in range(self.y_size):
			# remove all posible empty fields
			x = self.x_size-1
			while sum(self.numbers[y][:x+1]) != 0:
				if self.numbers[y][x] == 0:
					for i in range(x, 0, -1):
						self.numbers[y][i] = self.numbers[y][i-1]
					self.numbers[y][0] = 0
				else:
					x -= 1
			# add maching numbers
			for i in range(self.x_size-1, 0, -1):
				if self.numbers[y][i] == self.numbers[y][i-1]:
					self.numbers[y][i] *= 2
					self.score += self.numbers[y][i]
					for j in range(i-1, 0, -1):
						self.numbers[y][j] = self.numbers[y][j-1]
					self.numbers[y][0] = 0

	def left(self):
		self.past_numbers = self.numbers.copy()
		for y in range(self.y_size):
			# remove all posible empty fields
			x = 0
			while sum(self.numbers[y][x+1:]) != 0:
				if self.numbers[y][x] == 0:
					for i in range(x, self.x_size-1):
						self.numbers[y][i] = self.numbers[y][i+1]
					self.numbers[y][self.x_size-1] = 0
				else:
					x += 1
			# add maching numbers
			for i in range(self.x_size-1):
				if self.numbers[y][i] == self.numbers[y][i+1]:
					self.numbers[y][i] *= 2
					self.score += self.numbers[y][i]
					for j in range(i+1, self.x_size-1):
						self.numbers[y][j] = self.numbers[y][j+1]
					self.numbers[y][self.x_size-1] = 0

	def down(self):
		self.past_numbers = self.numbers.copy()
		for x in range(self.x_size):
			# remove all posible empty fields
			y = self.y_size-1			
			while sum(self.numbers[:y+1,x]) != 0:
				if self.numbers[y][x] == 0:
					for i in range(y, 0, -1):
						self.numbers[i][x] = self.numbers[i-1][x]
					self.numbers[0][x] = 0
				else:
					y -= 1
			# add maching numbers
			for i in range(self.y_size-1, 0, -1):
				if self.numbers[i][x] == self.numbers[i-1][x]:
					self.numbers[i][x] *= 2
					self.score += self.numbers[i][x]
					for j in range(i-1, 0, -1):
						self.numbers[j][x] = self.numbers[j-1][x]
					self.numbers[0][x] = 0

	def up(self):
		self.past_numbers = self.numbers.copy()
		for x in range(self.x_size):
			# remove all posible empty fields
			y = 0		
			while sum(self.numbers[y+1:,x]) != 0:
				if self.numbers[y][x] == 0:
					for i in range(y, self.y_size-1):
						self.numbers[i][x] = self.numbers[i+1][x]
					self.numbers[self.y_size-1][x] = 0
				else:
					y += 1
			# add maching numbers
			for i in range(self.y_size-1):
				if self.numbers[i][x] == self.numbers[i+1][x]:
					self.numbers[i][x] *= 2
					self.score += self.numbers[i][x]
					for j in range(i+1, self.y_size-1):
						self.numbers[j][x] = self.numbers[j+1][x]
					self.numbers[self.y_size-1][x] = 0

	def rollback(self):
		self.numbers = self.past_numbers.copy()

	def is_free_cell(self):
		return 0 in self.numbers

	# check if possibile to add numbers horizontally or vertically
	def is_dead_end(self):
		if self.is_free_cell():
			return False
		for i in range(self.y_size):
			for j in range(self.x_size-1):
				if self.numbers[i][j] == self.numbers[i][j+1]:
					return False
		for i in range(self.x_size):
			for j in range(self.y_size-1):
				if self.numbers[j][i] == self.numbers[j+1][i]:
					return False
		return True

	def get_score(self):
		return self.score

	def get_numbers(self):
		return self.numbers

	def get_past_numbers(self):
		return self.past_numbers