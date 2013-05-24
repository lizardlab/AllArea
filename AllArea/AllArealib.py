#edit the pi if you need it more or less digits
# For the shapes you want to calculate in your program you must
#declare the integers for that formula
pi = 3.1415
class Area:
	def rectangle(self):
		result = height*width
	def square(self):
		result = side** 2
	def triangle(self):
		result = width*height/2
	def circle(self):
		result = radius** 2 *pi
	def trapezoid(self):
		result = height/2 * (base1+base2)
	def pentagon(self):
		result = perimeter/2*apothem
	def hexagon(self):
		result = 1.5*height*side
	def recprism(self):
		result = 2*height*width+2*height*length+2*width*length
	def sphere(self):
		result = 4 * pi * radius**2
	def cone(self):
		result = pi*radius**2 + pi*slant
	def cylinder(self):
		result = 2*pi*radius*height + 2*pi*radius**2
	def ellipse(self):
		result = minor*major*pi
	def triprism(self):
		#you must define triangle which is the type of triangle
		if triangle == "equalateral":
			allArea.etrip();
		elif triangle == "isosceles":
			allArea.itrip();
		elif triangle == "scalene":
			allArea.strip();
		else:
			allArea.nshape();
	def etrip(self):
		result = base * height + base * length * 3
	def itrip(self):
		result = base*height+base*length+side*length*2
	def strip(self):
		result = height*side1+length*side1+length*side2+length*side3
	def pyramid(self):
		perimeter = width * 2 + length * 2
		result = perimeter * .5 * slant
	def cube(self):
		result = length**2 * 6
	def octagon(self):
		result = side**2 * 4.84
	def decagon(self):
		result = 2.5 * side * span
	def ngon(self):
		result = (nsides*side) * apothem / 2
	def nshape(self):
		print ("Shape not supported!")
allArea=Area();

