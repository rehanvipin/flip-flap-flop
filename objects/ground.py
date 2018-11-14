class Base(object):
	"""docstring for Base"""
	def __init__(self, body, x, y):
		self.body = body
		self.x = x
		self.y = y
		self.speed = 4

	def move(self, amt = 0, pos="Gibber"):
		if pos!="Gibber":
			self.x = pos	
		else:
			self.x += amt
