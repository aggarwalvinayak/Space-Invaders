import pygame
import time
import random

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



	if mouse_pos[0] < 535 and mouse_pos[0] > 270 and mouse_pos[1] < 480 and mouse_pos[1] > 400:#If mouse hovers over button
		pygame.draw.rect(screen, RED,(270,400,265,80))
		if mouse_click[0]:
			game_state = True
			Game()
	else:
		pygame.draw.rect(screen,BLUE,(270,400,265,80))

	text_welcome = font_times.render('START GAME', False, WHITE)
	screen.blit(text_welcome,(280,417))

def Game(): #The game has begin... initialize all classes and display
	pass

def Left(): #Move spaceship towards left
	pass

def Right(): #move spaceship towards right
	pass

##MAIN
WelcomeScreen() ## contains initial screen
game_state=False
quit=False
while not quit:
	if not game_state:
		WelcomeScreen()
	else:
		Game()

	for event in pygame.event.get():       
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				Left()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				Right()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				Fire_Spaceship()
		if event.type == pygame.QUIT:
			quit = True
    
	clock.tick(10) #Sets FPS of the game
	pygame.display.update()

pygame.quit()




