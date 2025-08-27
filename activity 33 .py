import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

# Set background color (Grey: 58, 58, 58)
bg_color = (58, 58, 58)

# Load image (make sure you have an image file in the same folder, e.g., "my_image.png")
image = pygame.image.load("my_image.png")
image = pygame.transform.scale(image, (300, 300))  # resize to 300x300

# Get rect and center the image
image_rect = image.get_rect(center=(250, 250))  # Center of 500x500 window

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill background
    screen.fill(bg_color)

    # Draw image
    screen.blit(image, image_rect)

    # Update display
    pygame.display.flip()
