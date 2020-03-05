#edit the pi if you need it more or less digits
# For the shapes you want to calculate in your program you must
#declare the integers for that formula
pi = 3.1415
class Volume:
	def vrecprism(self):
		result = height * width * length
	def vtriprism(self):
		result = height * width / 2 * length
	def vsphere(self):
		result = 4 * pi * radius**3 / 3
	def vpyramid(self):
		result = base * height / 3
	def vcone(self):
		result = pi* radius**2 * height / 3
	def vcylinder(self):
		result = pi * radius**2 * height
	def vpyramid(self):
		result = length * width / 3 * height
	def vcube(self):
		result = length**3
	def nobject(self):
		print ("Object not supported!")
allVolume=Volume();
