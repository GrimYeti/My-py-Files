"""
 Simple graphics demo
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
# Import a library of functions called 'pygame'
import pygame
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
PI = 3.141592653
 
# Set the height and width of the screen
size = (640, 480)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Cool Game")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    
    def draw_tree(x, y):
        pygame.draw.rect(screen, RED, [60+x, 170+y, 30, 45])
        pygame.draw.polygon(screen, GREEN, [[150+x,170+y],[75+x,20+y], [x,170+y]])
        pygame.draw.polygon(screen, GREEN, [[140+x,120+y], [75+x,y], [10+x,120+y]])
    
    def draw_house(x,y):
        pygame.draw.rect(screen,(255,171,244),(x,y-180,200,180))
        pygame.draw.rect(screen,(89,71,0),(x+80,y-60,40,60))
        pygame.draw.circle(screen,(255,204,0),(x+112,y-30),4)
        pygame.draw.polygon(screen, (125,125,125), ( (x,y-180),(x+100,y-250),(x+200,y-180) ) )
        draw_window(x+20,y-90)
        draw_window(x+130,y-90)
    
    def draw_window(x,y):
        pygame.draw.rect(screen,(207,229,255),(x,y-50,50,50))
        pygame.draw.rect(screen,(0,0,0),(x,y-50,50,50),5)
        pygame.draw.rect(screen,(0,0,0),(x+23,y-50,5,50))
        pygame.draw.rect(screen,(0,0,0),(x,y-27,50,5))
    
    
    def draw_cloud(x,y,size):
        pygame.draw.circle(screen,(255,255,255),(x,y),int(size*.5))
        pygame.draw.circle(screen,(255,255,255),(int(x+size*.5),y),int(size*.6))
        pygame.draw.circle(screen,(255,255,255),(x+size,int(y-size*.1)),int(size*.4))
    
    
    pygame.draw.rect(screen,(0,160,3),(0,400,640,80))
    pygame.draw.rect(screen,(135,255,255),(0,0,640,400))
    
    draw_tree(50,200)
    draw_tree(450,200)
    
    draw_house(225,400)
    
    draw_cloud(60,120,80)
    draw_cloud(200,50,40)
    draw_cloud(450,100,120)
    
 

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()