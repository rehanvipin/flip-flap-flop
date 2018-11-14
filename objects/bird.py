""" the bird object for the main game """

class Bird(object):
	def __init__(self, start_pos):
		super(Bird, self).__init__()
		self.x = start_pos[0]
		self.y = start_pos[1]
		self.height = 24
		self.width = 34
		self.theta = 0
		self.speed = 0

	def move(self, new_speed):
		self.speed = new_speed


		