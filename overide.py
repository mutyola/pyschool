import math
class shape:
	def _init_(self):
		print('call _init_ from shape class')

	def calculate_area(self):
		print('calling calculate_area() from shape class')
		return 0
class circle(shape):
	def __init__(self, r):
		print('call __init__ from circle class')
		self.r = r
	def calculate_area(self):
		print('calling calculate_area() from circle class')
		return math.pi * self.r * self.r
