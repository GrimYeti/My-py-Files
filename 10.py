"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screen=pygame.display.set_mode((700, 500))
screen_rect=screen.get_rect()
player=pygame.Rect(60, 170, 30, 45)
    #Trunk
pygame.Surface.polygon([150,170],[75,20], [170])
    #Leaves
pygame.Surface.polygon([140,120], [75], [10,120])
    #Leaves
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]: player.move_ip(0, -1)
            if keys[pygame.K_a]: player.move_ip(-1, 0)
            if keys[pygame.K_s]: player.move_ip(0, 1)
            if keys[pygame.K_d]: player.move_ip(1, 0)
            player.clamp_ip(screen_rect) # ensure player is inside screen
            screen.fill((255,255,255))
            pygame.draw.rect(screen, (0,0,0), player)
            pygame.display.flip()            
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()






#import pygame
#pygame.init()
#screen=pygame.display.set_mode((400, 400))
#screen_rect=screen.get_rect()
#player=pygame.Rect(180, 180, 20, 20)
#run=True
#while run:
    #for e in pygame.event.get():
        #if e.type == pygame.QUIT: run = False
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_w]: player.move_ip(0, -1)
    #if keys[pygame.K_a]: player.move_ip(-1, 0)
    #if keys[pygame.K_s]: player.move_ip(0, 1)
    #if keys[pygame.K_d]: player.move_ip(1, 0)
    #player.clamp_ip(screen_rect) # ensure player is inside screen
    #screen.fill((255,255,255))
    #pygame.draw.rect(screen, (0,0,0), player)
    #pygame.display.flip()