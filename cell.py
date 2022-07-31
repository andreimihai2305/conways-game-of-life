import pygame
from settings import *

class Cell(pygame.sprite.Sprite):

	def __init__(self, row, col):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.size = CELL_SIZE
		self.state = -1
		self.row = row
		self.col = col
		self.x = (self.col * self.size)
		self.y = (self.row * self.size)
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.neighbours = []
		self.living_neighbours = 0


	def __repr__(self):
		return f"Cell({self.row}, {self.col}, state={'Alive' if self.state == 1 else 'Dead'})"


	def change_state(self) -> None:
		self.state *= -1


	def get_living_neighbours(self):
		living_neighbours = 0
		for neighbour in self.neighbours:
			if neighbour.state == 1:
				living_neighbours += 1


		self.living_neighbours = living_neighbours


	def get_pos(self) -> int:
		return (self.row, self.col)


	def draw(self) -> None:
		if self.state == -1:
			pygame.draw.rect(self.display_surface, WHITE, self.rect, width=1)


		else:
			pygame.draw.rect(self.display_surface, WHITE, self.rect)


