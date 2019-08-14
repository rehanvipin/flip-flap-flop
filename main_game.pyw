
__doc__ = """ An advance spin off of a popular mobile game. """
__version__ = "1.0"
__author__ = "Ice Cold Articuno"

from sys import argv

import pygame

from objects import bird, pipes, ground
from time import sleep,time
from Database.verifier import opyt, writer
from game_constants import *

pygame.init()

bolt = bird.Bird(initial_position)

game_window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flip Flap")
game_clock = pygame.time.Clock()

if argv[-1] == "admin":
	debugger = True					# change this to True whenever you need to debug
else:
	debugger = False
restart_screen = False 					# change this to True to get a nicer restart screen

bolt.body = pygame.image.load('.\\Assets\\bluebird-midflap.png')
background = pygame.image.load('.\\Assets\\backgroundimg.png')
game_over_pic = pygame.image.load('.\\Assets\\gameover.png')
score_sprites = [pygame.image.load(f'.\\Assets\\{i}.png') for i in range(10)]

base = ground.Base(pygame.image.load('.\\Assets\\base.png'),base_x, base_y)


lower_pipes_30 = [pipes.Pipes(pygame.image.load('.\\Assets\\pipe-green.png'),200,0,0) for i in range(no_of_pipes)]	# for the lower pipes
upper_pipes_30 = [pipes.Pipes(pygame.image.load('.\\Assets\\pipe-green_up.png'),200,0,0) for i in range(no_of_pipes)]
pipes_start_pos = []		# for the position for the pipes at the beginning
lower_heights = []
lower_pipe_ht_diff = 70

opyt()						# checking if the scores have been tampered with

for i in range(len(lower_pipes_30)):			# making the lower pipes 
	lower_pipe_ht_diff = pipes.OG_RNG(lower_pipe_ht_diff)
	lower_pipes_30[i].x = 855 + lower_pipes_30[i].separation*i
	pipes_start_pos.append(lower_pipes_30[i].x)
	lower_pipes_30[i].y = 200 + lower_pipe_ht_diff	# a diff between 60 and 150 seems to be good
	lower_heights.append(lower_pipes_30[i].y - 200)

for i in range(len(upper_pipes_30)):			# initializing the lower pipes with their values
	upper_pipes_30[i].x = 855 + upper_pipes_30[i].separation*i
	upper_pipes_30[i].y = -200 - between + lower_heights[i]


def make_pipes():								# to put the pipes back to where they came from
	global lower_pipes_30, upper_pipes_30
	for i in range(len(lower_pipes_30)):
		lower_pipes_30[i].x = pipes_start_pos[i]				# to reset the pipes position after 30
		upper_pipes_30[i].x = pipes_start_pos[i]

def text_objects(text, font, text_color): #displays the font with the text with the font and returns the rectangele to display
	text_surface = font.render(text, True, colors[text_color])
	return text_surface, text_surface.get_rect()

def text_display(text,rect_centre, text_color, font_size):
	crash_text = pygame.font.Font('freesansbold.ttf',font_size) 
	text_surface, Text_rectangle = text_objects(text, crash_text, text_color) 
	Text_rectangle.center = (rect_centre) 
	game_window.blit(text_surface, Text_rectangle) 
	pygame.display.update()

def display_score(score,game_window,score_sprites):
	#text_display(str(score))			# fallback plan
	modif = list(map(int,str(score)))
	length = len(modif)
	score_start_pos_x = screen_width/2 - score_width*(length/2)
	score_start_pos_y = screen_height*0.1
	for i in range(length):
		posit = (score_start_pos_x+(score_width*i),score_start_pos_y)
		game_window.blit(score_sprites[modif[i]],posit)
		
def game_over(score,restart_screen):
	global bolt, game_window, game_clock
	#text_display('restart the game')
	game_window.blit(game_over_pic,((screen_width/2.6),screen_height/2.4))
	make_pipes()						# to make the pipes again
	if (argv[-1] != "admin"):
		write_scores(score, name =argv[1])					# to write the user's score to the file
	sort_scores()						# to sort the hishscores
	top_score = make_user_feel_bad()	# to get the highscore
	text_display('Highscore : ' + top_score,((screen_width/2),screen_height/20),'black',28)
	op_centre = (screen_width/2,screen_height/3.2)
	op = "game restarts in 3"

	for i in range(3):
		text_display(op,op_centre,'blue',30)
		pygame.display.update()
		sleep(1)
		op = str(2-i)
		op_centre = ((screen_width/2 + 40*(1+i) + 125),screen_height/3.2)

	#teaser(game_window,game_clock)		# I don't like this for some reason, maybe a better 'between game' screen could fix this
	bolt.y = initial_position[1]

	if restart_screen:
		teaser(game_window,game_clock)

	game_loop(game_window, game_clock, quit_game =False)

def load_bird_image(flight_position,paused,angle_deviation):
	global bolt
	if not paused:
		if (0.15 < flight_position <= 0.30) or (0.6 < flight_position < 0.78):
			bolt.body = pygame.image.load('.\\Assets\\bluebird-upflap.png')
		elif (0 < flight_position <= 0.15) or (0.45 < flight_position <= 0.6):
			bolt.body = pygame.image.load('.\\Assets\\bluebird-downflap.png')
		else:
			bolt.body = pygame.image.load('.\\Assets\\bluebird-midflap.png')
		bolt.theta += angle_deviation
		bolt.body = pygame.transform.rotate(bolt.body,angle_deviation)
	else:
		bolt.body = pygame.image.load('.\\Assets\\bluebird-midflap.png')

def teaser(game_window,game_clock):
	global bolt, base
	start = False
	while not start:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					start = True
			elif event.type == pygame.QUIT:
				pygame.quit()
			continue
		base.move(-4)

		if base.x < -100:
			base.move(pos=0)

		game_window.blit(background,(0,0))
		game_window.blit(base.body,(base.x,base.y))
		load_bird_image(-1,False,0)
		game_window.blit(bolt.body,(bolt.x,bolt.y))	
		text_display('PRESS SPACE TO START THE GAME',(screen_width/2,screen_height/3.2),'black',40)
		pygame.display.update()
		game_clock.tick(frames_per_second)

def game_loop(game_window,game_clock,quit_game,debugging=debugger):
	global bolt, base, between, background, angle_deviation

	score = 0
	start_time = time()
	bolt.speed = 3
	pipe_speed = 3
	angle_deviation = 0
	background_toggle = True
	pause = False
	crash = False

	while not quit_game:
		if bolt.speed  > 0:						# animation for the bird movement
			bolt.speed = ((bolt.speed)**2 + gravity_factor)**0.5
		elif bolt.speed == 0:
			bolt.speed = 0
		else:
			bolt.speed = -((bolt.speed)**2 + springiness)**0.5		# yeah, really! it do be like that

		if not crash:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						bolt.speed = -4
						angle_deviation += 15 
					elif event.key == pygame.K_SPACE:
						bolt.speed = -4
						angle_deviation += 15
					elif event.key == pygame.K_w:
						bolt.speed = -4
						angle_deviation += 15
					elif event.key == pygame.K_x:
						pause = True
					elif event.key == pygame.K_SPACE:
						pause = False
				if event.type == pygame.KEYUP and not pause:
					angle_deviation -= 13
					if angle_deviation > 20:
						angle_deviation = 10
					bolt.speed = 3				# just an optimal value to simulate gravity

		if bolt.y < 0:			# to make the bird bounce off the top of the screen, just in case...
			bolt.y == 0
			bolt.speed = 5

		if pause:				# this is for when the game is paused
			bolt.speed = 0
			base.speed = 0
			pipe_speed = 0
		elif not crash:			# don't remove this, it will cause the pipe_objects to stop moving
			base.speed = 3
			pipe_speed = 4

		if crash and (bolt.y + bolt.height) < base.y:	# when crashed
			bolt.speed = 3
			if angle_deviation > -90:
				angle_deviation -= 1.2
			base.speed = 0
			pipe_speed = 0

		if (bolt.y + bolt.height) == base.y:			# to quit the game when the bird has fallen down
			quit_game = True
			game_over(score,restart_screen)

		base.move(-1*base.speed)

		if base.x < -100:
			base.move(pos=0)

		if not pause:
			for i in range(len(lower_pipes_30)):
				lower_pipes_30[i].x = lower_pipes_30[i].x - pipe_speed		# to make the pipes move
				upper_pipes_30[i].x = upper_pipes_30[i].x - pipe_speed
				if ((bolt.x + bolt.width) >= lower_pipes_30[i].x) and (bolt.x <= (lower_pipes_30[i].x + pipe_width)):		# pipe crash logic
					if (bolt.y > (upper_pipes_30[i].y + pipe_height)) and ((bolt.y + bolt.height) < lower_pipes_30[i].y):
						if int(bolt.x) == lower_pipes_30[i].x and not crash:
							score += 1
					else:
						if not debugging :		
							crash = True
			if score%25 ==0 and score != 0:			# this is the code for the night mode
				if background_toggle:
					background = pygame.image.load('.\\Assets\\background-night.png')
				else:
					background = pygame.image.load('.\\Assets\\backgroundimg.png')
				background_toggle = not background_toggle
				score += 1
		else:
			text_display('PRESS SPACE TO CONTINUE',(screen_width/2,screen_height/3.2),'red',40) 					

		for i in range(len(lower_pipes_30)):
			if lower_pipes_30[no_of_pipes-1].x < 0:				# to make the game harder as it progresses
				if score == 20:
					between -= 20								# actually, check the logic of this again, it seems to be doing something weird
				elif score == 35:
					between -= 10
				elif score == 50:
					between -= 2
				elif score == 75:
					between -= 2
				lower_pipes_30[i].x = pipes_start_pos[i]				# to reset the pipes position after 30
				upper_pipes_30[i].x = pipes_start_pos[i]
				upper_pipes_30[i].y = -200 - between + lower_heights[i]
		
		bolt.y = bolt.y + bolt.speed # to move the bird up and down
		if bolt.y+bolt.height > 420:				# bird with ground crash logic
			bolt.y = screen_height*0.5
			game_over(score,restart_screen)
			quit_game = True

		game_window.blit(background,(0,0))	# to display the background
		flaps_time = start_time-time()
		flaps_time = int(flaps_time)-flaps_time
		load_bird_image(flaps_time,pause,angle_deviation)					# to make the bird flap(beta)
		if not crash:
			game_window.blit(bolt.body,(bolt.x,bolt.y))			# to display the bird

		for i in lower_pipes_30:
			game_window.blit(i.body,(i.x,i.y))		# to draw the pipes

		for i in upper_pipes_30:
			game_window.blit(i.body,(i.x,i.y))		# to draw the upper pipes

		game_window.blit(base.body,(base.x,base.y))		# to draw the base

		if crash:
			game_window.blit(bolt.body,(bolt.x,bolt.y))

		display_score(score,game_window,score_sprites)

		pygame.display.update()
		game_clock.tick(frames_per_second)

	return score

def main():
	pygame.init()
	teaser(game_window,game_clock)
	if argv[-1] == "admin":
		debugger = True
	else:
		debugger = False
	quit_game = False
	start_time = 0
	game_loop(game_window,game_clock,quit_game)
	writer()			# making a copy of the original scores.
	pygame.quit()

if __name__ == '__main__':
	argv.append(['loser'])
	main()