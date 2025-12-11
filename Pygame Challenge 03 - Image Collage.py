# -----------------------------------------------------------------------------
# IMAGE LAB - IMAGE COLLAGE
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different images to create a collage
# You can repeat the same images must use other commands to change the look (example, tint)

# LEVEL 4
# Everything listed in level 3 
# Create a scene with images

# LEVEL 4+
# Everything listed in level 4
# Randomize or animate something

# Recommended Lessons:
# P5.js intro
# P5.js drawing
# P5.js colour
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to githun when finished
# 
# Good luck!
#-----------------------------------------------------------------------------
import pygame
pygame.init()

window = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()

# ------- LOAD IMAGES -------
alien = pygame.transform.scale(pygame.image.load("Agartha.jpg"), (600,700))
can = pygame.transform.scale(pygame.image.load("Can.jpg"), (600,700))
mountain = pygame.transform.scale(pygame.image.load("Mountains.jpeg"), (600,700))

# ------- SCALE IMAGES -------
alien = pygame.transform.scale(alien, (250, 350))
can = pygame.transform.scale(can, (120, 250))
mountain = pygame.transform.scale(mountain, (600, 500))

# animation variable
can_x = 50
speed = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---- BACKGROUND ----
    window.blit(mountain, (0, 0))

    # ---- MAIN IMAGE (alien offering can) ----
    window.blit(alien, (300, 80))

    # ---- ANIMATED CAN ----
    window.blit(can, (can_x, 180))
    can_x += speed
    if can_x > 450 or can_x < 50:
        speed *= -1  # bounce left/right

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
