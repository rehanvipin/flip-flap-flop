""" the bird object for the main game """

class Bird(object):
	def __init__(self, start_pos):
		super(Bird, self).__init__()
		self.body = 0
		self.x = start_pos[0]
		self.y = start_pos[1]
		self.height = 24
		self.width = 34
		self.position = (self.x,self.y)
		self.theta = 0


		