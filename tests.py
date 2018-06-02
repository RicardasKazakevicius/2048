from grid import *

# test new numbers creation
numbers = Numbers(4,4)
numbers_to_add = 12	
for i in range(numbers_to_add):
	numbers.create_number()

used_cells = 0
for numbers_array in numbers.get():
	for number in numbers_array:
		if number != 0:
			used_cells += 1

assert numbers_to_add == used_cells

# test for rigth action
# y_size, x_size = 4, 4
# grid = Grid(x_size, y_size)
# for i in range(10):
#   grid.create_number()
# print grid.get_numbers()
# print
# # grid.action('right')
# # grid.action('left')
# grid.action('up')
# # grid.action('down')
# print grid.get_numbers()
# grid.back()
# print
# print grid.get_numbers()