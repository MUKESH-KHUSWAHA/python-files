#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      mukes
#
# Created:     20/08/2023
# Copyright:   (c) mukes 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Graphics")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(white)

    # Draw a blue rectangle
    pygame.draw.rect(screen, blue, (100, 100, 200, 150))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
