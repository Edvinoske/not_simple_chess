"""
The menu before starting a game
Menu example:
* Start game
* Load game
* Options
* Stats
* Achievements
* Exit
"""
from graphics import colors
import pygame

class dynamic_menu(object):
	"""
	A dynamic menu for the application
	"""
	def __init__(self, screen, items_array = [], title="Menu"):
		self.screen = screen
		self.title = title
		self.items_array = items_array
		self.font = pygame.font.SysFont("monospace", 15)

	def draw_menu(self):
		y_pos = 100
		for item in self.items_array:
			pygame.draw.rect(self.screen, colors.white, [self.screen.get_width() / 2 - 200, y_pos, 400, 50])
			text = self.font.render(item, 0, colors.black)
			self.screen.blit(text, [self.screen.get_width() / 2 - 200 + 2, y_pos + 2])
			y_pos += 70
