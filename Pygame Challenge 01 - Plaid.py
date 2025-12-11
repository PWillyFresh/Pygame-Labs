# -----------------------------------------------------------------------------
# COLOUR LAB - PLAID
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# The plaid must have 2 different colours
# LEVEL 4
# Everything listed in level 3 
# The plaid has 2 different strokeWeights
# LEVEL 4+
# Everything listed in level 4
# The plaid uses alpha colour
# 
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to github when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

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
import random
pygame.init()

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# ----- choose only TWO random colours at start -----
color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255), 120)
color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255), 120)
# ---------------------------------------------------

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))

    # surface for alpha
    s = pygame.Surface((500, 500), pygame.SRCALPHA)

    # horizontal lines (thick)
    for y in range(0, 500, 50):
        pygame.draw.line(s, color1, (0, y), (500, y), 12)

    # vertical lines (thin)
    for x in range(0, 500, 50):
        pygame.draw.line(s, color2, (x, 0), (x, 500), 4)

    window.blit(s, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
