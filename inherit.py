import math

class shape:
	def __init__(self):
		print('call __init__ from shape class')
	def foo(self):
		print('calling foo() from shape class')

class circle(shape):
	def __init__(self, r):
		print('call __init__ from circle class')
		self.r = r
	def calculate_area_circle(self):
		return math.pi * self.r * self.r

