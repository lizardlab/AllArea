#edit the pi if you need it more or less digits
pi = 3.1415
class Volume:
	def vrecprism(self):
		height = float(raw_input("What is the height?:"))
		width = float(raw_input("What is the width?:"))
		length = float(raw_input("What is the length?:"))
		result = height * width * length
		print ("Formula: height * width * length")
		print ("Result/Answer: " + str(result))
	def vtriprism(self):
		height = float(raw_input("What is the height?:"))
		width = float(raw_input("What is the width?:"))
		length = float(raw_input("What is the length?:"))
		result = height * width / 2 * length
		print ("Formula: height * width / 2 * length")
		print ("Result/Answer: " + str(result))
	def vsphere(self):
		radius = float(raw_input("What is the radius?:"))
		result = 4 * pi * radius**3 / 3
		print ("Formula: 4 * pi * radius^3 /3")
		print ("Result/Answer: " + str(result))
	def vpyramid(self):
		base = float(raw_input("What is the area of the base?:"))
		height = float(raw_input("What is the height?:"))
		result = base * height / 3
		print ("Formula: base * height / 3")
		print ("Result/Answer: " + str(result))
	def vcone(self):
		radius = float(raw_input("What is the radius?:"))
		height = float(raw_input("What is the height?:"))
		result = pi* radius**2 * height / 3
		print ("Formula: pi* radius^2 * height / 3")
		print ("Result/Answer: " + str(result))
	def vcylinder(self):
		radius = float(raw_input("What is the radius?:"))
		height = float(raw_input("What is the height?:"))
		result = pi * radius**2 * height
		print ("Formula: pi * radius^2 * height")
		print ("Result/Answer: " + str(result))
	def vpyramid(self):
		height = float(raw_input("What is the height?:"))
		width = float(raw_input("What is the width?:"))
		length = float(raw_input("What is the length?:"))
		result = length * width / 3 * height
		print ("Formula: length * width / 3 * height")
		print ("Result/Answer: " + str(result))
	def vcube(self):
		length = float(raw_input("What is the length?:"))
		result = length**3
		print ("Formula: length^3")
		print ("Result/Answer: " + str(result))
	def nobject(self):
		print ("Object not supported!")
object = raw_input("What is the object to calculate?:")
allVolume=Volume();
if object == "rectangular prism":
	allVolume.vrecprism();
elif object == "cuboid":
	allVolume.vrecprism();
elif object == "triangular prism":
	allVolume.vtriprism();
elif object == "sphere":
	allVolume.vsphere();
elif object == "pyramid":
	allVolume.vpyramid();
elif object == "cone":
	allVolume.vcone();
elif object == "cylinder":
	allVolume.vcylin();
elif object == "cube":
	allVolume.vcube();
else:
	allVolume.nobject();