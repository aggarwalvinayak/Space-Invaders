import pygame
import time
import random
from pygame.locals import *

#Initialze pygame
pygame.init()

#Defining RGB values for colours
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

screen = pygame.display.set_mode((800,650)) #Initialzing display
pygame.display.set_caption('SPACE INVADER') 
clock = pygame.time.Clock()

score=0

try:
	file_highscore=open("highscore.txt",'r') #reads highscore from text file
	file_highscore.seek(0,0)
	highest_score=int(file_highscore.read())
	file_highscore.close()
except:
	highest_score=0

def WelcomeScreen(): #initial screen before the game begins
	global quit,game_state
	mouse_pos=pygame.mouse.get_pos()
	mouse_click=pygame.mouse.get_pressed()
	screen.fill(GREY)

	logo = pygame.image.load('space-invaders-logo_transparent.png')
	screen.blit(logo,(30,80))



	if mouse_pos[0] < 535 and mouse_pos[0] > 270 and mouse_pos[1] < 480 and mouse_pos[1] > 400:
		pygame.draw.rect(screen, RED,(270,400,265,80))
		if mouse_click[0]:
			game_state = True
			Game()
	else:
		pygame.draw.rect(screen,BLUE,(270,400,265,80))

	text_welcome = font_times.render('START GAME', False, WHITE)
	screen.blit(text_welcome,(280,417))

def Game(): #The game has begin... initialize all classes and display
	global score,highest_score,ship,ship_y,ship_x

	background = pygame.image.load('background.png')
	screen.blit(background,(0,0))
	text_score = font_comic.render('SCORE:', False, GOLD)
	screen.blit(text_score,(150,25))
	text_score = font_comic.render(str(score), False, ORANGE)
	screen.blit(text_score,(270,25))
	text_score = font_comic.render('HIGH SCORE:', False, GOLD)
	screen.blit(text_score,(430,25))
	text_score = font_comic.render(str(highest_score), False, ORANGE)
	screen.blit(text_score,(630,25))
	Spaceship()


	#display all objects 
	pass

def Left_press(): #increase velocity
	global vel_ship
	vel_ship=-10
	pass

def Right_press(): #increase velocity
	global vel_ship
	vel_ship=10
	pass

def Release_arrowkey(): #velocity=0
	global vel_ship
	vel_ship=0
	pass

def Fire_Spaceship(): #release a bullet from same x coordinate upwards
	pass

def initial():
	global ship,ship_x,ship_y,vel_ship
	# Spaceship object and starting coordinates
	ship = font_comic.render('Ship',False,GOLD) # This line has to modified to get spaceship object
	ship_y = screen.get_height() - 50
	ship_x = screen.get_width()/2 - ship.get_width()/2
	vel_ship=0

# Function to change positon and display Spaceship
def Spaceship():
	global vel_ship,ship,ship_y,ship_x
	ship_x+=vel_ship
	if ship_x <= 0 + ship.get_width()/2: #stop if hits left wall
		ship_x-=vel_ship
		vel_ship=0
	if ship_x >= 800 - ship.get_width()/2: #stop if hits right wall
		ship_x-=vel_ship
		vel_ship=0
	screen.blit(ship,(ship_x,ship_y))

# Invader Object and Class
invader = font_comic.render('Invader',False,RED) # This line to be replaced by Invader image

class Invader:
	invader_x = random.randrange(0,screen.get_width())
	invader_y = random.randrange(0,400)
	def __init__(self,invader,invader_x,invader_y):
		self.invader = invader
		
	def get_invader(self):
		screen.blit(self.invader,(self.invader_x,self.invader_y))




##MAIN
WelcomeScreen() ## contains initial screen
game_state=False
quit=False
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
    
	clock.tick(20) #Sets FPS of the game
	pygame.display.update()

pygame.quit()




