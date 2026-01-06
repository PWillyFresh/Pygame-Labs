# -----------------------------------------------------------------------------
# TEXT & FONT LAB - RANSOM NOTE
# 
# Use your new knowledge of text in Pygame to make a ransom note similar to the picture above.
# 
# You use whatever fonts you want as long as you use at least 1 custom font.
# 
# The message can say whatever you want as long as it is school safe (remember the code of conduct).
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different font styles
# Use 3 different colours
# Write a message that is school safe and does not have anyone’s personal information (including names)

# LEVEL 4
# Everything listed in level 3 
# Use at least 4 different font styles
# Use 4 different colours

# LEVEL 4+
# Everything listed in level 4
# Use a custom downloaded font
# 
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# Pygame Text & Fonts
# 
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

# ---------- SETUP ----------
windowWidth = 500
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()

# ---------- FONTS ----------
font1 = pygame.font.Font("Font1.otf", 50)
font2 = pygame.font.Font("Font2.otf", 50)
font3 = pygame.font.Font("Font3.otf", 50)

fonts = [font1, font2, font3]

# ---------- MESSAGE ----------
words = ["JUST", "GIVE", "ME", "A", "DOLLAR"]

# ---------- POSITIONS (fixed so it isn't buggy) ----------
positions = [(30, 80), (200, 80), (30, 180), (200, 180), (120, 280)]

# ---------- RANDOM COLORS (only once when you start) ----------
colors = []
for i in range(len(words)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors.append((r, g, b))

    # ---------- RANDOM FONTS (only once when you start) ----------
chosen_fonts = []
for i in range(len(words)):
    chosen_fonts.append(random.choice(fonts))


# ---------- GAME LOOP ----------
running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))

    # draw each word once in a random color + random font
    for i, word in enumerate(words):
        font = chosen_fonts[i]
        color = colors[i]
        text = font.render(word, True, color)
        window.blit(text, positions[i])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
