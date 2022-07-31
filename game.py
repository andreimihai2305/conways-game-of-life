import pygame
from sys import exit
from settings import *
from grid import Grid


class Game():

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()
		self.grid = Grid()
		self.started = False

	# Main game loop
	def run(self):
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
					if event.type == pygame.MOUSEBUTTONUP:
						pos = pygame.mouse.get_pos()
						self.grid.check_click(pos)

			self.screen.fill(BLACK)
			if self.started:
				self.grid.update()
			self.grid.draw()
			pygame.display.update()
			
			self.clock.tick(FPS)					



# Running the game
if __name__ == "__main__":
	game_of_life = Game()
	game_of_life.run()