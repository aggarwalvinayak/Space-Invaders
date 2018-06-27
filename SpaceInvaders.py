import pygame
import time
import random
from pygame.locals import *

# Initialze pygame
pygame.init()

# Defining RGB values for colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (174, 182, 191)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (243, 156, 18)
GOLD = (230, 215, 0)

font_comic = pygame.font.SysFont('Comic Sans MS', 40)
font_times = pygame.font.SysFont('Times New Roman', 40)

screen = pygame.display.set_mode((800, 650))  # Initialzing display
pygame.display.set_caption('SPACE INVADER')
clock = pygame.time.Clock()

score = 0

try:
    file_highscore = open("highscore.txt", 'r')  # reads highscore from text file
    file_highscore.seek(0, 0)
    highest_score = int(file_highscore.read())
    file_highscore.close()
except:
    highest_score = 0


def WelcomeScreen():  # initial screen before the game begins
    global quit, game_state
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    screen.fill(GREY)

    logo = pygame.image.load('space-invaders-logo_transparent.png')
    screen.blit(logo, (30, 80))

    if mouse_pos[0] < 535 and mouse_pos[0] > 270 and mouse_pos[1] < 480 and mouse_pos[1] > 400:
        pygame.draw.rect(screen, RED, (270, 400, 265, 80))
        if mouse_click[0]:
            game_state = True
            Game()
    else:
        pygame.draw.rect(screen, BLUE, (270, 400, 265, 80))

    text_welcome = font_times.render('START GAME', False, WHITE)
    screen.blit(text_welcome, (280, 417))


def Game():  # The game has begin... initialize all classes and display
    global score, highest_score, ship, ship_y, ship_x, invader1a_list, invader1b_list, invader1c_list, invader2_list, invader3_list, invader_mys


    background = pygame.image.load('background.png')
    screen.blit(background, (0, 0))
    text_score = font_comic.render('SCORE:', False, GOLD)
    screen.blit(text_score, (150, 25))
    text_score = font_comic.render(str(score), False, ORANGE)
    screen.blit(text_score, (300, 25))
    text_score = font_comic.render('HIGH SCORE:', False, GOLD)
    screen.blit(text_score, (430, 25))
    text_score = font_comic.render(str(highest_score), False, ORANGE)
    screen.blit(text_score, (700, 25))

    Spaceship()
    for i in range(len(invader1a_list)):
        invader1a_list[i].Get_Invader()
        invader1b_list[i].Get_Invader()
        invader1c_list[i].Get_Invader()
    for i in range(len(invader2_list)):
        invader2_list[i].Get_Invader()
        invader3_list[i].Get_Invader()
    invader_mys.Get_Invader()

    # display all objects
    pass


def Left_press():  # increase velocity
    global vel_ship
    vel_ship = -10
    pass


def Right_press():  # increase velocity
    global vel_ship
    vel_ship = 10
    pass


def Release_arrowkey():  # velocity=0
    global vel_ship
    vel_ship = 0
    pass


def Fire_Spaceship():  # release a bullet from same x coordinate upwards
    pass


def initial():
    global ship, ship_x, ship_y, vel_ship, invader1a_list, invader1b_list, invader1c_list, invader2_list, invader3_list, invader_mys
    # Spaceship object and starting coordinates
    ship = pygame.image.load('tank.jpg').convert_alpha()  # This line has to modified to get spaceship object
    ship_y = screen.get_height() - 50
    ship_x = screen.get_width() / 2 - ship.get_width() / 2
    vel_ship = 0
    ##Initalise invaders
    invader1a_list = [Invader1(invader1, i, 300) for i in range(200, 650, 50)]
    invader1b_list = [Invader1(invader1, i, 265) for i in range(200, 650, 50)]
    invader1c_list = [Invader1(invader1, i, 230) for i in range(200, 650, 50)]
    invader2_list = [Invader2(invader2, i, 195) for i in range(220, 600, 40)]
    invader3_list = [Invader3(invader3, i, 160) for i in range(220, 600, 40)]
    invader_mys = Invader_Mystery(invaderM, 380, 120)


# Function to change positon and display Spaceship
def Spaceship():
    global vel_ship, ship, ship_y, ship_x
    ship_x += vel_ship
    if ship_x <= 0 + ship.get_width() / 2:  # stop if hits left wall
        ship_x -= vel_ship
        vel_ship = 0
    if ship_x >= 800 - ship.get_width() / 2:  # stop if hits right wall
        ship_x -= vel_ship
        vel_ship = 0
    screen.blit(ship, (ship_x, ship_y))


# Invader Class


invader1 = pygame.image.load('i1.jpg').convert_alpha()
invader2 = pygame.image.load('i3.jpg').convert_alpha() # This line to be replaced by Invader image
invader3 = pygame.image.load('i2.jpg').convert_alpha()  # This line to be replaced by Invader image
invaderM = pygame.image.load('i4.jpg').convert_alpha()


class Invader1:
    global score

    def __init__(self, invader1, invader_x, invader1_y):
        self.invader1 = invader1
        self.invader_x = invader_x
        self.invader_y = invader1_y

    def Get_Invader(self):
        screen.blit(self.invader1, (self.invader_x, self.invader_y))

    def Invader_Attack(self):
        score += 10


class Invader2:
    global score

    def __init__(self, invader2, invader_x, invader2_y):
        self.invader2 = invader2
        self.invader_x = invader_x
        self.invader_y = invader2_y

    def Get_Invader(self):
        screen.blit(self.invader2, (self.invader_x, self.invader_y))

    def Invader_Attack(self):
        score += 20


class Invader3:
    global score

    def __init__(self, invader3, invader_x, invader3_y):
        self.invader3 = invader3
        self.invader_x = invader_x
        self.invader_y = invader3_y

    def Get_Invader(self):
        screen.blit(self.invader3, (self.invader_x, self.invader_y))

    def Invader_Attack(self):
        score += 30


class Invader_Mystery:
    global score
    count = 0

    def __init__(self, invader_m, invader_x, invaderM_y):
        self.invaderM = invader_m
        self.invader_x = invader_x
        self.invader_y = invaderM_y

    def Get_Invader(self):
        screen.blit(self.invaderM, (self.invader_x, self.invader_y))

    def Invader_Attack(self):
        self.count += 1
        if count == 3:
            score += 100


# Bullet Class
bullet = font_comic.render('Bullet', False, BLACK)


class Bullet:
    global ship_x, ship_y

    def __init__(self, bullet):
        self.bullet = bullet
        self.bullet_x = ship_x + ship.get_width() / 2
        self.bullet_y = ship_y

    def Get_Bullet(self):
        screen.blit(self.bullet, (self.bullet_x, self.bullet_y))


##MAIN
WelcomeScreen()  ## contains initial screen
game_state = False
quit = False
initial()
while not quit:
    if not game_state:
        WelcomeScreen()
    else:
        Game()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Left_press()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Right_press()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Release_arrowkey()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Fire_Spaceship()
        if event.type == pygame.QUIT:
            quit = True

    clock.tick(20)  # Sets FPS of the game
    pygame.display.update()

pygame.quit()





