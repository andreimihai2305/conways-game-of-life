import pygame
from settings import *
from cell import Cell

class Grid():

	def __init__(self):
		# Get a list of the grid's cells 
		self.cells = [[Cell(i, j) for j in range(WIDTH // CELL_SIZE)] for i in range(HEIGHT // CELL_SIZE)]
		for row in self.cells:
			for cell in row:
				self.update_cell_neighbours(cell)



	# Draw Grid on screen
	def draw(self) -> None:
		for row in self.cells:
			for cell in row:
				cell.draw()


	# Check if a cell is selected
	def check_click(self, pos) -> None:
		for row in self.cells:
			for cell in row:
				if cell.rect.collidepoint(pos):
					cell.change_state()


	# Getting the list of neighbours for each cell
	def update_cell_neighbours(self, cell) -> None:
		neighbours = []
		try:
			neighbours.append(self.cells[cell.row - 1][cell.col -1])
			neighbours.append(self.cells[cell.row][cell.col -1])
			neighbours.append(self.cells[cell.row + 1][cell.col -1])

			neighbours.append(self.cells[cell.row - 1][cell.col])
			neighbours.append(self.cells[cell.row + 1][cell.col])

			neighbours.append(self.cells[cell.row - 1][cell.col + 1])
			neighbours.append(self.cells[cell.row][cell.col + 1])
			neighbours.append(self.cells[cell.row + 1][cell.col + 1])
		except IndexError:
			pass
			
		cell.neighbours = neighbours
		
	# Updating the game state
	def update(self) -> None:
		for row in self.cells:
			for cell in row:
				cell.get_living_neighbours()


		for row in self.cells:
			for cell in row:
				if cell.living_neighbours < 2 and cell.state == 1:
					cell.change_state()

				elif cell.living_neighbours > 3 and cell.state == 1:
					cell.change_state()

				elif cell.living_neighbours == 3 and cell.state == -1:
					cell.change_state()

				else:
					continue


	def reset(self) -> None:
		for row in self.cells:
			for cell in row:
				if cell.state == 1:
					cell.change_state()

		