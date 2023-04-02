import pygame
from sys import exit

def display_score():
    current_time = int((pygame.time.get_ticks() / 1000)) - start_time
    score_surf = font.render(f'Score {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time
    

pygame.init()   # Initialize pygame
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))  # Create a screen
pygame.display.set_caption("Runner")  # Set the title of the window
clock = pygame.time.Clock() # Create a clock object
font = pygame.font.Font('font/Blox2.ttf', 50)   # Create a font object
game_active = True
start_time = 0 # Set the start time of the game
score = 0

sky_surface = pygame.image.load('graphics/sky.png').convert() # Load the image and convert it to a surface
sky_surface = pygame.transform.scale(sky_surface, (screen_width, screen_height))

ground_surface = pygame.image.load('graphics/ground.png').convert() # Load the image and convert it to a surface
ground_height = 100  # Adjust this value based on the desired height of the ground
ground_surface = pygame.transform.scale(ground_surface, (screen_width, ground_height))

#text_surface = font.render('My Game', False, (64,64,64)) # Create a surface with the text
#score_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail.png').convert_alpha() # Load the image and convert it to a surface
original_width, original_height = snail_surface.get_size()
scaled_width, scaled_height = original_width * 3, original_height * 3
snail_surface = pygame.transform.scale(snail_surface, (scaled_width, scaled_height))
snail_rect = snail_surface.get_rect(bottomright = (700, screen_height - ground_height))

player_surface = pygame.image.load('graphics/player_walk/p2_walk01.png').convert_alpha() # Load the image and convert it to a surface
player_rect = player_surface.get_rect(midbottom = (80, screen_height - ground_height))
player_gravity = 0
player_stand = pygame.image.load('graphics/player_walk/p2_walk03.png').convert_alpha() # Load the image and convert it to a surface
player_stand = pygame.transform.rotozoom(player_stand, 90, 2)
player_Stand_rect = player_stand.get_rect(center = (400, 200))

game_name = font.render('Martian Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 75))

game_message = font.render('Press Space to Run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (390, 340))

while True:
    for event in pygame.event.get():    # Get all events
        if event.type == pygame.QUIT:   # If the event is quit
            pygame.quit()               # Quit pygame
            exit()                      # Quit python
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= screen_height - ground_height:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= screen_height - ground_height:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
    
    if game_active:
        screen.blit(sky_surface,(0,0))                                           # Draw the surface on the screen
        screen.blit(ground_surface,(0, screen_height - ground_height))         # Draw the surface on the screen
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)                            # Draw the surface on the screen
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(text_surface, score_rect)                                   # Draw the surface on the screen
        score = display_score()
        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = screen_width
        snail_y_pos = player_rect.bottom - scaled_height            # adjusts snail position to player position
        screen.blit(snail_surface, snail_rect)                      # Draw the surface on the screen

        #PLAYER MOVEMENT
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= screen_height - ground_height:
            player_rect.bottom = screen_height - ground_height
            player_gravity = 0
        screen.blit(player_surface, player_rect)                    # Draw the surface on the screen

        #collision detection
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_Stand_rect)

        score_message = font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 325))
        screen.blit(game_name, game_name_rect)
        if score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)
        
        
        # draw all elements
        # update everything
    pygame.display.update() # Update the screen
    clock.tick(60)  # Set the framerate to 60 fps
