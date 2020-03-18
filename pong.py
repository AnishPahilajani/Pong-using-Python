import pygame
from random import *
import time
import winsound as wn

BLACK = (0,0,0)
class ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([45, 45])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the paddle (a rectangle!)
        #pygame.draw.rect(self.image, color, [0, 0, width, height])
        pygame.draw.circle(self.image, color, [10, 10], 10)
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def move_ran(self, ball_target): 
        #moving the ball
        if ball.move == "downR":
            #print("going down")
            self.rect.x += 5
            self.rect.y += 5
        elif ball.move == "upR":
            self.rect.x += 5
            self.rect.y -= 5
        elif ball.move == "upL":
            self.rect.x -= 5
            self.rect.y -= 5
        elif ball.move == "downL":
            self.rect.x -= 5
            self.rect.y += 5
            
            
        #Check that you are not going too far (off the screen)
        if ball_target == "Right":
            if self.rect.y < 0:
                ball.move = "downR"
            if self.rect.y >= 465:
                ball.move = "upR"
        elif ball_target == "Left":
            if self.rect.y < 10:
                ball.move = "downL"
            if self.rect.y >= 465:
                ball.move = "upL"
            
            
        if self.rect.x > 700:
            
            self.rect.x = 340
            self.rect.y = 210
        if self.rect.x < 0:
            
            self.rect.x = 340
            self.rect.y = 210



BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y > 400:
          self.rect.y = 400





# Import the pygame library and initialise the game engine
# from paddle import Paddle
# from ball import Ball
 
pygame.init()


 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Open a new window
sizew = (700, 500)
screenw = pygame.display.set_mode(sizew)
pygame.display.set_caption("Pong winner")


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

 # Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = ball(WHITE, 10, 10)
ball.rect.x = 340
ball.rect.y = 210


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    
    
    

    



def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
         
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                intro = False
                
        screen.fill(WHITE)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Pong", largeText)
        TextRect.center = ((size[0]/2),(size[1]/2))
        screen.blit(TextSurf, TextRect)

        button("Start",150,450,100,50,green,bright_green,game)
            
        
        pygame.display.update()
        clock.tick(15)


def game():

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    win = False
    # Add the car to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True


    #Initialise player scores
    scoreA = 0
    scoreB = 0

    ball.move = "downR"

    ball_target = "Right"
    ran = 0
    A = 0
    B = 0
    

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                         carryOn=False


        #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)    

        # --- Game logic should go here
        all_sprites_list.update()
        # when ball bounces
        if ball.rect.x == 650 and ball.rect.y < (paddleB.rect.y+ 88) and ball.rect.y > (paddleB.rect.y - 22):
            ball_target = "Left"
            ran = randint(0, 1)
            wn.Beep(500, 20)
            if ran == 1:
                ball.move = "upL"
                ran = 1
                
            if ran == 0:
                ball.move = "downL"
                ran = 0

                
        elif ball.rect.x == 25 and ball.rect.y < (paddleA.rect.y+ 88) and ball.rect.y > (paddleA.rect.y - 19):
            wn.Beep(500, 20)
            ball_target = "Right"
            ran = randint(0, 1)
            if ran == 1:
                ball.move = "downR"
                ran = 1
                
            if ran == 0:
                ball.move = "upR"
                ran = 0
                
        elif win == True:
            time.sleep(5)
            game_intro()
            
        if ball.rect.x >= 700:
            A += 1
            
        if ball.rect.x <= 0:
            B+=1
                
        ball.move_ran(ball_target)
        

        # First, clear the screen to black. 
        screen.fill(BLACK)
        #Draw the net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen) 
        
        # --- Drawing code should go here
        font = pygame.font.SysFont("comicsansms", 70)
        text = font.render(str(B), True, WHITE)
        screen.blit(text,(500 - text.get_width() // 2, 100 - text.get_height() // 2))
        
        font = pygame.font.SysFont("comicsansms", 70)
        text = font.render(str(A), True, WHITE)
        screen.blit(text,(200 - text.get_width() // 2, 100 - text.get_height() // 2))
        f = 0
        if A >= 11:
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Player A wins", True, bright_green)
            screenw.blit(text,(350 - text.get_width() // 2, 300 - text.get_height() // 2))
            win = True
        elif B >= 11:
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Player B wins", True, bright_red)
            screenw.blit(text,(350 - text.get_width() // 2, 300 - text.get_height() // 2))
            win = True
            
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:

game_intro()
game()
pygame.quit()