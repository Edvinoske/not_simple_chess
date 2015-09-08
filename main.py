import pygame
import game_engine
import graphics
import main_menu
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Not Simple Chess")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates, or FPS.
clock = pygame.time.Clock()
 
# ---------- Main Program Loop ----------

while not done:

	# ---------- Main event loop ----------

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
 
	# ----------- Game logic should go here -----------
 
	# ---------- Drawing code should go here ----------
 
	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	screen.fill(WHITE)
	
	# Draw main menu
	main_menu.draw_main_menu()
 
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
	# --- Limit to 60 frames per second
	clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()