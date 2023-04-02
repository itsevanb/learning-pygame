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

text_surface = font.render('My Game', False, (64,64,64)) # Create a surface with the text
score_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail.png').convert_alpha() # Load the image and convert it to a surface
original_width, original_height = snail_surface.get_size()
scaled_width, scaled_height = original_width * 2, original_height * 2
snail_surface = pygame.transform.scale(snail_surface, (scaled_width, scaled_height))
snail_rect = snail_surface.get_rect(bottomright = (600, screen_height - ground_height))

player_surface = pygame.image.load('graphics/player_walk/p2_walk01.png').convert_alpha() # Load the image and convert it to a surface
player_rect = player_surface.get_rect(midbottom = (80, screen_height - ground_height))

while True:
    for event in pygame.event.get():    # Get all events
        if event.type == pygame.QUIT:   # If the event is quit
            pygame.quit()               # Quit pygame
            exit()                      # Quit python
        #if event.type == pygame.MOUSEMOTION:
            #if player_rect.collidepoint(event.pos): print('collision')
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_SPACE:
                #print('jump')
    
    screen.blit(sky_surface,(0,0))                                           # Draw the surface on the screen
    screen.blit(ground_surface,(0, screen_height - ground_height))         # Draw the surface on the screen
    pygame.draw.rect(screen, '#c0e8ec', score_rect)                            # Draw the surface on the screen
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(text_surface, score_rect)                                   # Draw the surface on the screen
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = screen_width
    snail_y_pos = player_rect.bottom - scaled_height            # adjusts snail position to player position
    screen.blit(snail_surface, snail_rect)                      # Draw the surface on the screen
    screen.blit(player_surface, player_rect)                    # Draw the surface on the screen

    #keys = pygame.key.get_pressed()
    #keys[pygame.K_SPACE]:
    #print('jump')

    #if player_rect.colliderect(snail_rect):                     #Checks if the snail and player collide
        #print("Collision")

    """ mos_pos = pygame.mouse.get_pos()                            # Get the mouse position
    if player_rect.collidepoint(mos_pos):
        print(pygame.mouse.get_pressed())   """                     # Get the mouse button pressed
    
    
    
    # draw all elements
    # update everything
    pygame.display.update() # Update the screen
    clock.tick(60)  # Set the framerate to 60 fps
