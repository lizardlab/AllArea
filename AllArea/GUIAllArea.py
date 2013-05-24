#edit the pi if you need it more or less digits
pi = 3.14
from Tkinter import *

class Area:
	def start(self):
		self.question = Label(self.frame, text="Which shape would you like?")
		self.question.pack()
		self.rect = Button(self.frame, text="Rectangle", bg = "violet", command = self.rectangle)
		self.rect.pack()
		self.squa = Button(self.frame, text="Square", bg = "purple", command = self.square)
		self.squa.pack()
		self.tria = Button(self.frame, text="Triangle", bg = "blue", command = self.triangle)
		self.tria.pack()
		self.circ = Button(self.frame, text="Circle", bg = "green", command = self.circle)
		self.circ.pack()
		self.trap = Button(self.frame, text="Trapezoid", bg = "yellow", command = self.trapezoid)
		self.trap.pack()
		self.pent = Button(self.frame, text="Pentagon", bg = "orange", command = self.pentagon)
		self.pent.pack()
		self.hexa = Button(self.frame, text="Hexagon", bg = "red", command = self.hexagon)
		self.hexa.pack()
		self.recp = Button(self.frame, text="RectPrism", bg = "violet", command = self.recprism)
		self.recp.pack()
		self.sphe = Button(self.frame, text="Sphere", bg = "purple", command = self.sphere)
		self.sphe.pack()
		self.cone = Button(self.frame, text="Cone", bg = "blue", command = self.cone)
		self.cone.pack()
		self.cyli = Button(self.frame, text="Cylinder", bg = "green", command = self.cylinder)
		self.cyli.pack()
		self.elli = Button(self.frame, text="Ellipse", bg = "yellow", command = self.ellipse)
		self.elli.pack()
		self.triprism = Button(self.frame, text="TriPrism", bg = "orange", command = self.triprism)
		self.triprism.pack()
		self.pyramid = Button(self.frame, text="Pyramid", bg = "red", command = self.pyramid)
		self.pyramid.pack()
		self.cube = Button(self.frame, text="Cube", bg = "violet", command = self.cube)
		self.cube.pack()
		self.sector = Button(self.frame, text="Sector", bg = "purple", command = self.sector)
		self.sector.pack()
		self.octagon = Button(self.frame, text="Octagon", bg = "blue", command = self.octagon)
		self.octagon.pack()
		self.decagon = Button(self.frame, text="Decagon", bg = "green", command = self.decagon)
		self.decagon.pack()
		self.ngon = Button(self.frame, text="N-gon", bg = "yellow", command = self.ngon)
		self.ngon.pack()
	def __init__(self, master):
		print "Hello."

		self.master = master #copy it for the future
		self.welcome = Label(master, text="Welcome to AllArea.py\n")
		self.welcome.pack()

		self.frame = Frame(master)
		self.frame.pack()

		self.quitb = Button(self.frame, text="QUIT", fg="red", bg="black", command=self.frame.quit)
		self.quitb.pack()

		self.startb = Button(self.frame, text="START", fg="green", bg="blue", command=self.start)
		self.startb.pack()
	def rectangle(self):
		q1 = Label(self.frame, text="What is the width?")
		q2 = Label(self.frame, text="What is the height?")
		self.width = Entry(self.frame)
		self.height = Entry(self.frame)

		q1.pack()
		self.width.pack()
		q2.pack()
		self.height.pack()
		submit = Button(self.frame, text = "Submit", fg = "blue", bg = "white", command = self.calcrect)
		submit.pack()
	def calcrect(self):
		formula = Label(self.frame, text="Formula: width * height")
		formula.pack()
		height = float(self.height.get())
		width = float(self.width.get())
		result = width * height

		res = Label(self.frame, text="Result/Answer: "+str(result))
		res.pack()
	def square(self):
		q1 = Label(self.frame, text="What is the length?")
		self.length = Entry(self.frame)

		q1.pack()
		self.length.pack()
		self.submit = Button(self.frame, text = "Submit", fg = "blue", bg="white", command = self.calcsqua)
		self.submit.pack()
	def calcsqua(self):
		formula = Label(self.frame, text="Formula: length^2")
		length = float(self.length.get())
		result = length** 2

		res = Label(self.frame, text="Result/Answer: "+str(result))
		formula.pack()
		res.pack()
	def triangle(self):
		q1 = Label(self.frame, text="What is the base?")
		q2 = Label(self.frame, text="What is the height?")
		self.base = Entry(self.frame)
		self.height = Entry(self.frame)

		q1.pack()
		self.base.pack()
		q2.pack()
		self.height.pack()
		self.submit = Button(self.frame, text = "Submit", fg = "blue", bg = "white", command = self.calctria)
		self.submit.pack()
	def calctria(self):
		formula = Label(self.frame, text="Formula: .5 * height * base")
		base = float(self.base.get())
		height = float(self.height.get())
		result = 0.5 * base * height

		res = Label(self.frame, text="Result/Answer: "+str(result))
		formula.pack()
		res.pack()
	def circle(self):
		q1 = Label(self.frame, text="What is the radius?")
		self.radius = Entry(self.frame)

		q1.pack()
		self.radius.pack()
		submit = Button(self.frame, text = "Submit", fg = "blue", bg = "white", command = self.calccirc)
		submit.pack()
	def calccirc(self):
		formula = Label(self.frame, text="Formula: radius^2 * pi")
		radius = float(self.radius.get())
		result = (radius ** 2) * pi

		res = Label(self.frame, text="Result/Answer: " + str(result))
		formula.pack()
		res.pack()
	def trapezoid(self):
		q1 = Label(self.frame, text="What is base 1?")
		q2 = Label(self.frame, text="What is base 2?")
		q3 = Label(self.frame, text="What is the height?")
		self.base1 = Entry(self.frame)
		self.base2 = Entry(self.frame)
		self.height = Entry(self.frame)

		q1.pack()
		self.base1.pack()
		q2.pack()
		self.base2.pack()
		q3.pack()
		self.height.pack()
		submit = Button(self.frame, text = "Submit", fg = "blue", bg = "white", command = self.calctrap)
		submit.pack()
	def calctrap(self):
		formula = Label(self.frame, text="Formula: height * .5 * (base1+base2)")
		formula.pack()
		base1 = float(self.base1.get())
		base2 = float(self.base2.get())
		height = float(self.height.get())
		result = height * .5 * (base1+base2)

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def pentagon(self):
		q1 = Label(self.frame, text="What is the apothem?")
		q2 = Label(self.frame, text="What is the perimeter?")
		self.apothem = Entry(self.frame)
		self.perimeter = Entry(self.frame)

		q1.pack()
		self.apothem.pack()
		q2.pack()
		self.perimeter.pack()
		submit = Button(self.frame, text = "Submit", fg = "blue",bg = "white", command = self.calcpent)
		submit.pack()
	def calcpent(self):
		formula = Label(self.frame, text="Formula: perimeter / 2 * apothem")
		formula.pack()
		apothem = float(self.apothem.get())
		perimeter = float(self.perimeter.get())
		result = perimeter / 2 * apothem

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def hexagon(self):
		q1 = Label(self.frame, text="What is the side length?")
		q2 = Label(self.frame, text="What is the height?")
		self.side = Entry(self.frame)
		self.height= Entry(self.frame)

		q1.pack()
		self.side.pack()
		q2.pack()
		self.height.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calchexa)
		submit.pack()
	def calchexa(self):
		formula = Label(self.frame, text="Formula: 1.5 * height * side")
		formula.pack()
		side = float(self.side.get())
		height = float(self.height.get())
		result = 1.5 * height * side

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def recprism(self):
		q1 = Label(self.frame, text="What is the height?")
		q2 = Label(self.frame, text="What is the length?")
		q3 = Label(self.frame, text="What is the width?")
		self.height = Entry(self.frame)
		self.length = Entry(self.frame)
		self.width = Entry(self.frame)

		q1.pack()
		self.height.pack()
		q2.pack()
		self.length.pack()
		q3.pack()
		self.width.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcrecp)
		submit.pack()
	def calcrecp(self):
		formula = Label(self.frame, text="Formula: 2*height*width + 2*height*length + 2*width*length")
		formula.pack()
		height = float(self.height.get())
		length = float(self.length.get())
		width = float(self.width.get())
		result = 2*height*width+2*height*length+2*width*length

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def sphere(self):
		q1 = Label(self.frame, text="What is the radius?")
		self.radius = Entry(self.frame)

		q1.pack()
		self.radius.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcsphe)
		submit.pack()
	def calcsphe(self):
		formula = Label(self.frame, text="Formula: 4 * pi *radius^2")
		formula.pack()
		radius = float(self.radius.get())
		result = 4 * pi * radius**2

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def cone(self):
		q1 = Label(self.frame, text="What is the slant length?")
		q2 = Label(self.frame, text="What is the radius?")
		self.slant = Entry(self.frame)
		self.radius = Entry(self.frame)

		q1.pack()
		self.slant.pack()
		q2.pack()
		self.radius.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calccone)
		submit.pack()
	def calccone(self):
		formula = Label(self.frame, text="Formula: pi*radius^2 + pi*slant")
		formula.pack()
		slant = float(self.slant.get())
		radius = float(self.radius.get())
		result = pi*radius**2 + pi*slant

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def cylinder(self):
		q1 = Label(self.frame, text="What is the radius?")
		q2 = Label(self.frame, text="What is the height?")
		self.radius = Entry(self.frame)
		self.height = Entry(self.frame)

		q1.pack()
		self.radius.pack()
		q2.pack()
		self.height.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calccyli)
		submit.pack()
	def calccyli(self):
		formula = Label(self.frame, text="Formula: 2*pi*radius*height + 2*pi*radius^2")
		formula.pack()
		radius = float(self.radius.get())
		height = float(self.radius.get())
		result = 2*pi*radius*height + 2*pi*radius**2

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def ellipse(self):
		q1 = Label(self.frame, text="What is half of the minor axis?")
		q2 = Label(self.frame, text="What is the half of the major axis?")
		self.minor = Entry(self.frame)
		self.major = Entry(self.frame)

		q1.pack()
		self.minor.pack()
		q2.pack()
		self.major.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcelli)
		submit.pack()
	def calcelli(self):
		formula = Label(self.frame, text="Formula: minor * major * pi")
		formula.pack()
		minor = float(self.minor.get())
		major = float(self.major.get())
		result = result = minor*major*pi

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def triprism(self):
		q1 = Label(self.frame, text="What type of triangle?")
		q1.pack()
		self.equalateral = Button(self.frame, text="Equalateral", fg = "white", bg = "blue", command = self.etrip)
		self.equalateral.pack()
		self.isosceles = Button(self.frame, text="Isosceles", fg = "white", bg = "blue", command = self.itrip)
		self.isosceles.pack()
		self.scalene = Button(self.frame, text="Scalene", fg = "white", bg = "blue", command = self.strip)
		self.scalene.pack()
	def etrip(self):
		q1 = Label(self.frame, text="What is the height?")
		q2 = Label(self.frame, text="What is the base?")
		q3 = Label(self.frame, text="What is the length?")
		self.height = Entry(self.frame)
		self.base = Entry(self.frame)
		self.length = Entry(self.frame)

		q1.pack()
		self.height.pack()
		q2.pack()
		self.base.pack()
		q3.pack()
		self.length.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcetrip)
		submit.pack()
	def itrip(self):
		q1 = Label(self.frame, text="What is the height?")
		q2 = Label(self.frame, text="What is the length?")
		q3 = Label(self.frame, text="What is the the base?")
		q4 = Label(self.frame, text="What is the triangle side length?")
		self.height = Entry(self.frame)
		self.length = Entry(self.frame)
		self.base = Entry(self.frame)
		self.side = Entry(self.frame)
		q1.pack()
		self.height.pack()
		q2.pack()
		self.length.pack()
		q3.pack()
		self.base.pack()
		q4.pack()
		self.side.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcitrip)
		submit.pack()
	def strip(self):
		q1 = Label(self.frame, text="What is the height?")
		q2 = Label(self.frame, text="What is the length?")
		q3 = Label(self.frame, text="What is the length of side 1?")
		q4 = Label(self.frame, text="What is the length of side 2?")
		q5 = Label(self.frame, text="What is the length of side 3?")
		self.height = Entry(self.frame)
		self.length = Entry(self.frame)
		self.side1 = Entry(self.frame)
		self.side2 = Entry(self.frame)
		self.side3 = Entry(self.frame)
		q1.pack()
		self.height.pack()
		q2.pack()
		self.length.pack()
		q3.pack()
		self.side1.pack()
		q4.pack()
		self.side2.pack()
		q5.pack()
		self.side3.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcstrip)
		submit.pack()
	def calcstrip(self):
		formula = Label(self.frame, text="Formula: height*side1+ length*side1+ length*side2+ length*side3")
		formula.pack()
		height = float(self.height.get())
		length = float(self.length.get())
		side1 = float(self.side1.get())
		side2 = float(self.side2.get())
		side3 = float(self.side3.get())
		result = height*side1+length*side1+length*side2+length*side3
		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def calcetrip(self):
		formula = Label(self.frame, text="Formula: base * height + base * length * 3")
		formula.pack()
		base = float(self.base.get())
		height = float(self.height.get())
		length = float(self.length.get())
		result = base * height + base * length * 3

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def calcitrip(self):
		formula = Label(self.frame, text="Formula: base*height + base*length + side*length*2")
		formula.pack()
		height = float(self.height.get())
		base = float(self.base.get())
		side = float(self.side.get())
		result = base*height+base*length+side*length*2

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def pyramid(self):
		q1 = Label(self.frame, text="What is the slant length?")
		q2 = Label(self.frame, text="What is the height?")
		q3 = Label(self.frame, text="What is the length?")
		q4 = Label(self.frame, text="What is the width?")
		self.slant = Entry(self.frame)
		self.height = Entry(self.frame)
		self.length = Entry(self.frame)
		self.width = Entry(self.frame)

		q1.pack()
		self.slant.pack()
		q2.pack()
		self.height.pack()
		q3.pack()
		self.length.pack()
		q4.pack()
		self.width.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcpyramid)
		submit.pack()
	def calcpyramid(self):
		formula = Label(self.frame, text="Formula: perimeter * .5 * slant")
		formula.pack()
		slant = float(self.slant.get())
		height = float(self.height.get())
		width = float(self.width.get())
		length = float(self.length.get())
		perimeter = width * 2 + length * 2
		result = perimeter * .5 * slant
		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def cube(self):
		q1 = Label(self.frame, text="What is the length?")
		self.length = Entry(self.frame)

		q1.pack()
		self.length.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calccube)
		submit.pack()
	def calccube(self):
		formula = Label(self.frame, text="Formula: length^2 * 6")
		formula.pack()
		length = float(self.length.get())
		result = length**2 * 6

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def sector(self):
		q1 = Label(self.frame, text="What is the radius?")
		q2 = Label(self.frame, text="What is the angle in radians?")
		self.radius = Entry(self.frame)
		self.radian = Entry(self.frame)

		q1.pack()
		self.radius.pack()
		q2.pack()
		self.radian.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcsector)
		submit.pack()
	def calcsector(self):
		formula = Label(self.frame, text="Formula: .5*radius^2*radian")
		formula.pack()
		radius = float(self.radius.get())
		radian = float(self.radian.get())
		result = .5 * radius**2 * radian

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def octagon(self):
		q1 = Label(self.frame, text="What is the length of the side?")
		self.side = Entry(self.frame)

		q1.pack()
		self.side.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcoctagon)
		submit.pack()
	def calcoctagon(self):
		formula = Label(self.frame, text="Formula: side^2 * 4.84")
		formula.pack()
		side = float(self.side.get())
		result = side**2 * 4.84

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def decagon(self):
		q1 = Label(self.frame, text="What is the length of the side?")
		q2 = Label(self.frame, text="What is the span?")
		self.side = Entry(self.frame)
		self.span = Entry(self.frame)

		q1.pack()
		self.side.pack()
		q2.pack()
		self.span.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcdecagon)
		submit.pack()
	def calcdecagon(self):
		formula = Label(self.frame, text="Formula: 2.5 * side * span")
		formula.pack()
		side = float(self.side.get())
		span = float(self.span.get())
		result = 2.5 * side * span

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def ngon(self):
		q1 = Label(self.frame, text="What is the number of sides?")
		q2 = Label(self.frame, text="What is the length of a side?")
		q3 = Label(self.frame, text="What is the length of the apothem?")
		self.nsides = Entry(self.frame)
		self.side = Entry(self.frame)
		self.apothem = Entry(self.frame)
		
		q1.pack()
		self.nsides.pack()
		q2.pack()
		self.side.pack()
		q3.pack()
		self.apothem.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.calcngon)
		submit.pack()
	def calcngon(self):
		formula = Label(self.frame, text="Formula: (# of sides*side) *apothem /2")
		formula.pack()
		nsides = float(self.nsides.get())
		side = float(self.side.get())
		apothem = float(self.apothem.get())
		result = (nsides*side) * apothem /2
		
		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
root = Tk()
allArea=Area(root);
root.mainloop()
