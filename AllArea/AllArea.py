#edit the pi if you need it more or less digits
pi = 3.1415
class Area:
	def rectangle(self):
		width = float(raw_input("What is the width?:"))
		height = float(raw_input("What is the height?:"))
		result = height*width
		print ("Formula: width * height")
		print ("Result/Answer: " + str(result))
	def square(self):
		side = float(raw_input("What is the length?:"))
		result = side** 2
		print ("Formula: side^2")
		print ("Result/Answer: " + str(result))
	def triangle(self):
		width = float(raw_input("What is the width?:"))
		height = float(raw_input("What is the height?:"))
		result = width*height/2
		print ("Formula: width * height / 2")
		print ("Result/Answer: " + str(result))
	def circle(self):
		radius = float(raw_input("What is the radius?:"))
		result = radius** 2 *pi
		print ("Formula: radius^2 * pi")
		print ("Result/Answer: " + str(result))
	def trapezoid(self):
		base1 = float(raw_input("What is base 1?:"))
		base2 = float(raw_input("What is base 2?:"))
		height = float(raw_input("What is the height?:"))
		result = height/2 * (base1+base2)
		print ("Formula: height * .5 * (base1 + base2)")
		print ("Result/Answer: " + str(result))
	def pentagon(self):
		apothem = float(raw_input("What is the apothem?:"))
		side = float(raw_input("What is the length of a side?:"))
		result = (side*5) *apothem /2
		print ("Formula: (side*5) * apothem /2")
		print ("Result/Answer: " + str(result))
	def hexagon(self):
		side = float(raw_input("What is the side length?:"))
		height = float(raw_input("What is the height?:"))
		result = 1.5*height*side
		print ("Formula: 1.5 * height * side")
		print ("Result/Answer: " + str(result))
	def recprism(self):
		height =  float(raw_input("What is the height?:"))
		width = float(raw_input("What is the width?:"))
		length = float(raw_input("What is the length?:"))
		result = 2*height*width+2*height*length+2*width*length
		print ("Formula: 2*height*width + 2*height*length + 2*width*length")
		print ("Result/Answer: " + str(result))
	def sphere(self):
		radius = float(raw_input("What is the radius?:"))
		result = 4 * pi * radius**2
		print ("Formula: 4 * pi *radius^2")
		print ("Result/Answer: " + str(result))
	def cone(self):
		slant = float(raw_input("What is the slant length?:"))
		radius = float(raw_input("What is the radius?:"))
		result = pi*radius**2 + pi*slant
		print ("Formula: pi*radius^2 + pi*slant")
		print ("Result/Answer: " + str(result))
	def cylinder(self):
		radius = float(raw_input("What is the radius?:"))
		height = float(raw_input("What is the height?:"))
		result = 2*pi*radius*height + 2*pi*radius**2
		print ("Formula: 2*pi*radius*height + 2*pi*radius*radius")
		print ("Result/Answer: " + str(result))
	def ellipse(self):
		minor = float(raw_input("What is half of the minor axis?:"))
		major = float(raw_input("What is half of the major axis?:"))
		result = minor*major*pi
		print ("Formula: minor * major * pi")
		print ("Result/Answer: " + str(result))
	def triprism(self):
		print ("Equalateral, Isosceles, Scalene")
		triangle = raw_input("What type?:")
		if triangle == "equalateral":
			allArea.etrip();
		elif triangle == "isosceles":
			allArea.itrip();
		elif triangle == "scalene":
			allArea.strip();
		else:
			allArea.nshape();
	def etrip(self):
		height = float(raw_input("What is the height?:"))
		length = float(raw_input("What is the length?:"))
		base = float(raw_input("What is the base?:"))
		result = base * height + base * length * 3
		print ("Formula: base * height + base * length * 3")
		print ("Result/Answer: " + str(result))
	def itrip(self):
		height = float(raw_input("What is the height?:"))
		length = float(raw_input("What is the length?:"))
		base = float(raw_input("What is the base?:"))
		side = float(raw_input("What is the side?:"))
		result = base*height+base*length+side*length*2
		print ("Formula: base*height + base*length + side*length*2")
		print ("Result/Answer: " + str(result))
	def strip(self):
		height = float(raw_input("What is the height?:"))
		length = float(raw_input("What is the length?:"))
		side1 = float(raw_input("What is the length of side1?:"))
		side2 = float(raw_input("What is the length of side2?:"))
		side3 = float(raw_input("What is the length of side3?:"))
		result = height*side1+length*side1+length*side2+length*side3
		print ("Formula: height*side1+ length*side1+ length*side2+ length*side3")
		print ("Result/Answer: " + str(result))
	def pyramid(self):
		slant = float(raw_input("What is the slant length?:"))
		height = float(raw_input("What is the height?:"))
		width = float(raw_input("What is the width?:"))
		length = float(raw_input("What is the length?:"))
		perimeter = width * 2 + length * 2
		result = perimeter * .5 * slant
		print ("Formula: perimeter * .5 * slant")
		print ("Result/Answer: " + str(result))
	def cube(self):
		length = float(raw_input("What is the length?:"))
		result = length**2 * 6
		print ("Formula: length^2 * 6")
		print ("Result/Answer: " + str(result))
	def octagon(self):
		side = float(raw_input("What is the length of the side?:"))
		result = side**2 * 4.84
		print ("Formula: side^2 * 4.84")
		print ("Result/Answer: " + str(result))
	def decagon(self):
		side = float(raw_input("What is the length of the side?:"))
		span = float(raw_input("What is the span?:"))
		result = 2.5 * side * span
		print ("Formula: 2.5 * side * span")
		print ("Result/Answer: " + str(result))
	def ngon(self):
		nsides = float(raw_input("How many sides are there?:"))
		side = float(raw_input("What is the length of one side?:"))
		apothem = float(raw_input("What is the length of the apothem?:"))
		result = (nsides*side) * apothem / 2
		print ("Formula: (# of sides*side) *apothem /2")
		print ("Result/Answer: " + str(result))
	def nshape(self):
		print ("Shape not supported!")
shape = raw_input("What type of shape to calculate:")
allArea=Area();
if shape == "rectangle":
	allArea.rectangle();
elif shape == "paralellogram":
	allArea.rectangle();
elif shape == "square":
	allArea.square();
elif shape == "triangle":
	allArea.triangle();
elif shape == "circle":
	allArea.circle();
elif shape == "trapezoid":
	allArea.trapezoid();
elif shape == "pentagon":
	allArea.pentagon();
elif shape == "hexagon":
	allArea.hexagon();
elif shape == "rectangular prism":
	allArea.recprism();
elif shape == "cuboid":
	allArea.recprism();
elif shape == "sphere":
	allArea.sphere();
elif shape == "cone":
	allArea.cone();
elif shape == "cylinder":
	allArea.cylinder();
elif shape == "ellipse":
	allArea.ellipse();
elif shape == "triangular prism":
	allArea.triprism();
elif shape == "pyramid":
	allArea.pyramid();
elif shape == "sector":
	allArea.sector();
elif shape == "cube":
	allArea.cube();
elif shape == "octagon":
	allArea.octagon();
elif shape == "decagon":
	allArea.decagon();
elif shape == "regular polygon":
	allArea.ngon();
elif shape == "ngon":
	allArea.ngon();
else:
	allArea.nshape();
