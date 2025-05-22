from abc import ABC, abstractmethod
 
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass
	@abstractmethod
	def volume(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
		
	def perimeter(self):
		return 2 * 3.14 * self.radius
	
	def area(self):
		return 3.14 * self.radius ** 2
	
	def volume(self):
		return 3.14 * 4 * self.radius ** 2

class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
	def perimeter(self):
		return 2 * (self.width + self.height)
	
	def area(self):
		return self.width * self.height
	def volume(self,depth):
		self.depth = depth
		return self.width * self.height * self.depth


class Square(Shape):
	def __init__(self, length):
		self.length = length
		
	def perimeter(self):
		return 4 * (self.length)
	
	def area(self):
		return self.length ** 2
	def volume(self):
		return self.length ** 3
	

