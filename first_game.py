import pygame
from sys import exit

pygame.init()   # Initialize pygame
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))  # Create a screen
pygame.display.set_caption("Runner")  # Set the title of the window
clock = pygame.time.Clock() # Create a clock object
font = pygame.font.Font('font/Blox2.ttf', 50)   # Create a font object

sky_surface = pygame.image.load('graphics/sky.png').convert() # Load the image and convert it to a surface
sky_surface = pygame.transform.scale(sky_surface, (screen_width, screen_height))

ground_surface = pygame.image.load('graphics/ground.png').convert() # Load the image and convert it to a surface
ground_height = 100  # Adjust this value based on the desired height of the ground
ground_surface = pygame.transform.scale(ground_surface, (screen_width, ground_height))

text_surface = font.render('My Game', False, 'Red') # Create a surface with the text

snail_surface = pygame.image.load('graphics/snail.png').convert_alpha() # Load the image and convert it to a surface
original_width, original_height = snail_surface.get_size()
scaled_width, scaled_height = original_width * 2, original_height * 2
snail_surface = pygame.transform.scale(snail_surface, (scaled_width, scaled_height))
snail_x_pos = 600

player_surface = pygame.image.load('graphics/player_walk/p2_walk01.png').convert_alpha() # Load the image and convert it to a surface
player_rect = player_surface.get_rect(midbottom = (80, screen_height - ground_height))

while True:
    for event in pygame.event.get():    # Get all events
        if event.type == pygame.QUIT:   # If the event is quit
            pygame.quit()               # Quit pygame
            exit()                      # Quit python
    
    screen.blit(sky_surface,(0,0))      # Draw the surface on the screen
    screen.blit(ground_surface,(0, screen_height - ground_height))         # Draw the surface on the screen
    screen.blit(text_surface,(300,50))         # Draw the surface on the screen
    snail_x_pos -= 3
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos, screen_height - ground_height))         # Draw the surface on the screen
    screen.blit(player_surface, player_rect)                 # Draw the surface on the screen

    # draw all elements
    # update everything
    pygame.display.update() # Update the screen
    clock.tick(60)  # Set the framerate to 60 fps
