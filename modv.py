from math import *

class City:
    # class data
    city_count = 0
    city_id = 0
    
     # constructor
    def __init__(self, name='', x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        City.city_count += 1  # access all City classes
        self.city_id = City.city_count

    def __str__(self):
        return 'City: ' + self.name + ',id=' + str(self.city_id) + ',x=' + str(self.x) + ',y=' + str(self.y)