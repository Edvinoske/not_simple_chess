import pygame
import game.game_engine
from graphics import background, colors
from interface import main_menu

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Not Simple Chess")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
print("Game is ready!")
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            print event

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(colors.black)

	# Draw main menu
    menu = main_menu.dynamic_menu(screen, ["New Game", "Load Game", "Options", "Quit"])
    menu.draw_menu()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
