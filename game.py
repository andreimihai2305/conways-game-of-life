import pygame
from sys import exit
from settings import *
from grid import Grid


class Game():

	def __init__(self) -> None:
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Conwa's Game of Life")
		self.clock = pygame.time.Clock()
		self.grid = Grid()
		self.started = False


	def __call__(self) -> None:
		self.run()

	# Main game loop
	def run(self) -> None:
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.started = not self.started
					elif event.key == pygame.K_r and not self.started:
						self.grid.reset()

				if not self.started:
					if event.type == pygame.MOUSEBUTTONDOWN:
						pos = pygame.mouse.get_pos()
						self.grid.check_click(pos)

			self.screen.fill(BLACK)
			if self.started:
				self.grid.update()
			self.grid.draw()
			pygame.display.update()
			
			self.clock.tick(FPS)