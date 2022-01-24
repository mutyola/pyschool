from math import *
class City:
	# class data
	city_count = 0
	city_id = 0
	### do something
	# class attributes
	def move_to(self, x=0, y=0):
		self.x += x
		self.y += y
	def distance(self, other_city):
		xi = pow(other_city.x - self.x, 2)
		yi = pow(other_city.y - self.y, 2)
		return sqrt(xi + yi)