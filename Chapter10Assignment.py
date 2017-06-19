"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)


#Function to draw stickfigure at X and Y variable
def draw_house(screen, x, y):
    #House
    pygame.draw.rect(screen,(128,128,0),(x,y-180,200,180))
    
    #Door
    pygame.draw.rect(screen,(89,71,0),(x+80,y-60,40,60))
    
    #Door Knob
    pygame.draw.circle(screen,(255,204,0),(x+112,y-30),4)
    
    #Roof
    pygame.draw.polygon(screen, (125,125,125), ( (x,y-180),(x+100,y-250),(x+200,y-180) ) )
    draw_window(x+20,y-90)
    draw_window(x+130,y-90)    


def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BROWN, [60+x, 170+y, 30, 45])
    #Trunk
    pygame.draw.polygon(screen, GREEN, [[150+x,170+y],[75+x,20+y], [x,170+y]])
    #Leaves
    pygame.draw.polygon(screen, GREEN, [[140+x,120+y], [75+x,y], [10+x,120+y]])
    #Leaves
    
#Windows for house
def draw_window(x,y):
        pygame.draw.rect(screen,(207,229,255),(x,y-50,50,50))
        pygame.draw.rect(screen,(0,0,0),(x,y-50,50,50),5)
        pygame.draw.rect(screen,(0,0,0),(x+23,y-50,5,50))
        pygame.draw.rect(screen,(0,0,0),(x,y-27,50,5))
    

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

snow_list = []
 
pygame.display.set_caption("Connor B's Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Star/Snow code
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 425)
    snow_list.append([x, y])

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
     
        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
     
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
                
            
    # --- Main event loop
    
 
    # --- Game logic should go here
    
    
    
    #Code to make sure tree does not go off the screen. 
    if x_coord > 550:
        x_coord = 550
    if x_coord < 0:
        x_coord = 0
    if y_coord > 300:
        y_coord = 300
    if y_coord < 0:
        y_coord = 0
    
    
  
    
        
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    
    #Ground 
    pygame.draw.rect(screen,(0,160,3),(0,425,700,80))   
    
    # Process each snow flake/Star in the list
    for i in range(len(snow_list)):
     
    # Draw the snow flake/Star
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)    
    
  
    # Game logic
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    
    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed
     
    # Draw the tree
    draw_tree(screen, x_coord, y_coord)
    
     
    # Drawing section
    draw_house(screen, x, y)    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()