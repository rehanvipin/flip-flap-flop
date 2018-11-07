import re as witchcraft

# really important constants, feel free to edit and save them if you notice any improvements
colors = {'black':(0,0,0),'white':(255,255,255),'red':(200,30,30),'green':(0,255,0),'blue':(20,30,200)}
screen_height = 512
screen_width = 855
initial_position = (screen_width*0.5,screen_height*0.5)
frames_per_second = 150
base_x = 0
base_y = 420
base_speed = 3
pipe_separation = 100
pipe_toughness = 50
no_of_pipes = 25
pipe_height = 320
pipe_width = 52
between = 30
springiness = 1			# +/- 2 only
gravity_factor = 0.5	# keep below 1.5
score_width = 24

# Have to modify the write_scores, but the rest are fine, you needn't change them

def write_scores(score,name='loser'):
	with open('scores.LOG','a') as records:
		log = '\n'+ name +'\'s score: ' + str(score)
		records.write(log)

random_buffer = []

def sort_scores():
	global random_buffer
	with open('scores.LOG','r') as filler:
		random_buffer = list(filler)
	random_buffer = list(filter(lambda x : not x.isspace(),random_buffer))
	random_buffer = list(map(lambda x:x.rstrip('\n').lstrip('\n'),random_buffer))
	random_buffer = sorted(random_buffer,key = lambda x:int(witchcraft.search('\d+',x).group()))
	random_buffer = random_buffer[:1] + list(filter(lambda x: int(x[-1]),random_buffer))

	with open('scores.LOG','w') as wiper:
		for i in random_buffer:
			buffers = '\n' + i
			wiper.write(buffers)

	with open('hiscor','w') as tops:
		high_score = random_buffer[-1]
		high_score = witchcraft.search(r'\d+',high_score).group()
		tops.write(high_score)

def make_user_feel_bad():
	with open('hiscor','r') as drugs:
		return drugs.read()
