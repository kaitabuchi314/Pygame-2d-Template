import pygame
from pygame.locals import *


#color defenitions
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
LIGHT_BLUE = (0, 200, 240)
LIGHT_ORANGE = (240, 200, 0)

#init window
pygame.init()
displayInfo = pygame.display.Info()
screen = pygame.display.set_mode((1000, 500))
background = pygame.image.load("bg.png").convert_alpha(screen)
pygame.mouse.set_visible(False)

#init game
running = True
mouse_pos = None
player_pos = (0,0)
player_image = pygame.image.load("player.png").convert_alpha(screen)

#functions
def draw_sprite(sprite, position):
	screen.blit(sprite, position)

def draw_bg():
	screen.blit(background, (0,0))
	#screen.fill(background)

#Game Loop
while running:
	for event in pygame.event.get():
		#close the window if user commands
		if event.type == pygame.QUIT:
			running = False

		#draw Background
		draw_bg()

		#game logic

		mouse_pos = pygame.mouse.get_pos()
		player_pos = mouse_pos
		player_pos = (player_pos[0] - (player_image.get_width() / 2), player_pos[1] - (player_image.get_height() / 2))

		#draw sprites
		draw_sprite(player_image, player_pos)
		#end frame
		pygame.display.update()

pygame.quit()