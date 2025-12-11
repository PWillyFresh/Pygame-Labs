# -----------------------------------------------------------------------------
# ANIMATION LAB - SCROLLING BACKGROUND
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# A background that scrolls across the screen creating the illusion of movement
# LEVEL 4+
# Everything listed in level 3 
# Multiple layers moving at different speeds to create the parallax effect, like you see to the left
# 
# Recommended Lessons:
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# Pygame Images
# Pygame Animation
# 
# Challenge Difficulty:*
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to githunb when finished
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
pygame.init()

# ---------- SETUP ----------
windowWidth = 500
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()

# ---------- LOAD IMAGE ----------
bg_image = pygame.image.load("Forest.png")
bg_image = pygame.transform.scale(bg_image, (windowWidth, windowHeight))

# ---------- VARIABLES ----------
x = 0          # current x position of image
scroll_speed = 2  # speed of scrolling

# ---------- GAME LOOP ----------
running = True
while running:
    # ---- EVENTS ----
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    # ---- UPDATE ----
    x = x - scroll_speed
    if x <= -windowWidth:  # reset when image fully off-screen
        x = 0

    # ---- DRAW ----
    window.blit(bg_image, (x, 0))
    window.blit(bg_image, (x + windowWidth, 0))  # draw second copy for seamless scroll

    # ---- SHOW FRAME ----
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
