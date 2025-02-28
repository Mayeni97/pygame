import pygame
import sys

pygame.init()
# Set up the display
Screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Tile Size
TILESIZE = 50

# Floor
floor_image = pygame.image.load("assets/floor.png").convert_alpha()
floor_image = pygame.transform.scale(floor_image, (TILESIZE * 20, TILESIZE * 5))
floor_rect = floor_image.get_rect(bottomleft=(0, Screen.get_height()))

# Player
player_image = pygame.image.load("assets/player_static.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (TILESIZE, TILESIZE * 2))
player_rect = player_image.get_rect(center=(Screen.get_width() / 2, Screen.get_height() - floor_image.get_height() - (player_image.get_height() / 2)))


# apple
apple_image = pygame.image.load("assets/apple.png").convert_alpha()
apple_image = pygame.transform.scale(apple_image, (TILESIZE, TILESIZE))
apple  
running = True 

def update ():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

def draw():
    Screen.fill("skyblue")
    Screen.blit(floor_image, floor_rect)
    Screen.blit(player_image, player_rect.topleft)
    
# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    update()        
    draw()        
            
    clock.tick(60)
    pygame.display.update()
