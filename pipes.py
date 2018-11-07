import random
from game_constants import pipe_toughness
class Pipes:
	def __init__(self, image, separation, x, y):
		self.body = image
		self.separation = separation
		self.x = x
		self.y = y
def OG_RNG(prev=0):					# to make the pipes height's variation higher
	mixer = random.SystemRandom()
	rng = random.randint(50,180)
	while abs(rng-prev) < pipe_toughness:		# change pipe toughness in game constants to make the game tougher
		rng = random.randrange(60,150)
	return rng