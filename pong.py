import pygame
from pygame.locals import *
import random,math

BALLSPEED = 0.2
PADDLESPEED = 0.5
BALLSPEEDFACTORINCREASE = 0.2
MAXBOUNCEANGLE = 5*math.pi/(math.radians(12))
GOALSTOWIN = 2

#Class of the player
class PlayerPaddle(object):
    #Initialize Player Object
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = 0+5
        self.centery = int(screensize[1]*0.5)

        self.height = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5), self.width, self.height)

        self.color = (100,255,100)

        self.speed = PADDLESPEED
        self.direction = 0

    #Function update of the player in game
    def update(self):
        self.centery += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)
        
        #Check to see the player object is not outbounds
        if self.rect.top < 0:
            self.rect.top = 0
            self.direction = 0
        if self.rect.bottom > self.screensize[1]-1:
            self.rect.bottom = self.screensize[1]-1
            self.direction = 0
            
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)
    
#CPU Paddle
class AIPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.height = 100
        self.width = 10

        self.centerx = screensize[0]-5
        self.centery = int(screensize[1]*0.5)

        self.rect = pygame.Rect(screensize[0]-5, self.centery-int(self.height*0.5), self.width, self.height)
        
        self.color = (255,100,100)

        self.speed = PADDLESPEED

    def update(self, ball):
        #AI to check if the ball is in a distance of 15% of the paddle to it's start moving 
        if ball.rect.x > self.screensize[0] - (self.screensize[0] * 0.15): 
            if ball.rect.top < self.rect.top:
                self.centery -= self.speed
            elif ball.rect.bottom > self.rect.bottom:
                self.centery += self.speed
        
        #Ajust the position
        self.rect.center = (self.centerx, self.centery)        

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)
    
    def lose(self, screen, i):
        pygame.draw.rect(screen, (0,0,0), (0, self.centery-int(self.height*0.5), self.width, i), 0)

#Class of the ball
class Ball(object):
    def __init__(self, screensize):

        self.screensize = screensize

        self.centerx = int(screensize[0]*0.5)
        self.centery = int(screensize[1]*0.5)

        self.radius = 8

        self.rect = pygame.Rect(self.centerx-self.radius,
                                self.centery-self.radius,
                                self.radius*2, self.radius*2)

        self.color = (255,255,255)

        #Randoms the position the ball will go at the start 
        self.direction = [random.randrange(-1,2,2), random.randrange(-1,2,2)]
        self.speedx = BALLSPEED
        self.speedy = BALLSPEED
       
        self.hit_playerGoal = False
        self.hit_aiGoal = False
        self.hit_edge_top = False
        self.hit_edge_bot = False

    def update(self, playerPaddle, aiPaddle):
        self.centerx += self.direction[0]*self.speedx
        self.centery += self.direction[1]*self.speedy

        self.rect.center = (self.centerx, self.centery)

        #Check if the ball collide with the walls
        if self.rect.right >= self.screensize[0]-1:
            self.hit_aiGoal = True
        elif self.rect.left <= 0:
            self.hit_playerGoal = True
        elif self.rect.top <= 0:
            self.direction[1] *= -1
        elif self.rect.bottom >= self.screensize[1]-1:
            self.direction[1] *= -1

        #Check colission of the ball with the paddles
        if self.rect.colliderect(playerPaddle.rect):
            self.direction[0] *= -1
            ballSpeedIncrease = BALLSPEED + BALLSPEEDFACTORINCREASE
            bounceAngle = calculateAngle(playerPaddle.rect.y, playerPaddle.height/2, self.rect.y)
            self.speedx = ballSpeedIncrease * math.cos(bounceAngle)
            self.speedy = ballSpeedIncrease * -math.sin(bounceAngle)
        if self.rect.colliderect(aiPaddle.rect):
            self.direction[0] *= -1 
            ballSpeedIncrease = BALLSPEED + BALLSPEEDFACTORINCREASE
            bounceAngle = calculateAngle(aiPaddle.rect.y, aiPaddle.height/2, self.rect.y)
            self.speedx = ballSpeedIncrease * math.cos(bounceAngle)
            self.speedy = ballSpeedIncrease * -math.sin(bounceAngle)

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (0,0,0), self.rect.center, self.radius, 1)

#Calculate the angle that the ball will go after colliding with a paddle
def calculateAngle(paddleY, paddleHalfHeight, ballY):
    relativeIntersectY = (paddleY + paddleHalfHeight) - ballY
    normalizedRealtiveIntersectY = (relativeIntersectY/(paddleHalfHeight))
    return normalizedRealtiveIntersectY * MAXBOUNCEANGLE

#Main Class
def main():
    pygame.init()
    
    screensize = (1024,512)
    screen = pygame.display.set_mode(screensize)
    
    endgame = False
    win = False
    
    #Define font of the text
    myfont = pygame.font.SysFont('Comic Sans MS',40)

    winner = myfont.render("WINNER!", 1, (0,0,255))
    loser = myfont.render("Try Again!", 1, (255,0,0))   
    
    #Initialize objects
    player_paddle = PlayerPaddle(screensize)
    aiPaddle = AIPaddle(screensize)
    ball = Ball(screensize)
    
    score_player = 0 
    score_ai = 0
    
    running = True
    #Starts the loop to render game
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    #Check collision upper side
                    if player_paddle.rect.top <= 0:
                        player_paddle.direction = 0
                    else:
                        player_paddle.direction = -1
                elif event.key == K_DOWN:
                    #Check collision down side
                    if player_paddle.rect.bottom >= screensize[1]:
                        player_paddle.direction = 0
                    else:
                        player_paddle.direction = 1
        
            if event.type == KEYUP:
                #Lock the paddle to not go further up or down screen
                if event.key == K_UP and player_paddle.direction == -1:
                    player_paddle.direction = 0
                elif event.key == K_DOWN and player_paddle.direction == 1:
                    player_paddle.direction = 0

        #Check if ball hit the player side wall
        if ball.hit_playerGoal:
            score_ai += 1
            ball = Ball(screensize)
            label_ai = myfont.render(str(score_ai),1,(255,255,255))

        #Check if ball hit the CPU side wall
        if ball.hit_aiGoal:
            score_player += 1
            ball = Ball(screensize)
            label_player = myfont.render(str(score_player),1,(255,255,255))

        #Condition to end the game
        if score_player == GOALSTOWIN:
            endgame = True
            win = True
        if score_ai == GOALSTOWIN:
            endgame = True

        #Update objects in screen
        player_paddle.update()
        aiPaddle.update(ball)
        ball.update(player_paddle, aiPaddle)

        #renderization
        screen.fill((128,128,128))
        player_paddle.render(screen)
        aiPaddle.render(screen)
        ball.render(screen)
        label_ai = myfont.render(str(score_ai),1,(255,255,255))
        label_player = myfont.render(str(score_player),1,(255,255,255))
        screen.blit(label_player, (screensize[0]/4, screensize[1]/2))
        screen.blit(label_ai, (screensize[0]/1.5, screensize[1]/2))

        #Check if the game ended
        while endgame:
            running = False
            pygame.display.update()
            if win:
                #Show winner message
                screen.blit(winner, (screensize[0]/2-100, screensize[1]/2-100))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        endgame = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                            endgame = False    
            else:
                #Show loser message
                screen.blit(loser, (screensize[0]/2-100, screensize[1]/2-100))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        endgame = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                            endgame = False  

        # Flip the display
        pygame.display.flip()

    pygame.quit()

main()