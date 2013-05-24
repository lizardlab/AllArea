#edit the pi if you need more or less digits
from Tkinter import *
pi = 3.1415
class Volume:
	def __init__(self, master):
		print "Hello."

		self.master = master
		self.welcome = Label(master, text="Welcome to AllVolume.py\n")
		self.welcome.pack()

		self.frame = Frame(master)
		self.frame.pack()

		self.quitb = Button(self.frame, text="QUIT", fg="red", bg="black", command=self.frame.quit)
		self.quitb.pack()

		self.startb = Button(self.frame, text="START", fg="green", bg="blue", command=self.start)
		self.startb.pack()
	def start(self):
		self.question = Label(self.frame, text="Which object would you like?")
		self.question.pack()
		self.recp = Button(self.frame, text="RectPrism", bg = "violet", command = self.vrecprism)
		self.recp.pack()
		self.sphe = Button(self.frame, text="Sphere", bg = "purple", command = self.vsphere)
		self.sphe.pack()
		self.cone = Button(self.frame, text="Cone", bg = "blue", command = self.vcone)
		self.cone.pack()
		self.cyli = Button(self.frame, text="Cylinder", bg = "green", command = self.vcylinder)
		self.cyli.pack()
		self.triprism = Button(self.frame, text="TriPrism", bg = "orange", command = self.vtriprism)
		self.triprism.pack()
		self.pyramid = Button(self.frame, text="Pyramid", bg = "red", command = self.vpyramid)
		self.pyramid.pack()
		self.cube = Button(self.frame, text="Cube",bg = "violet", command = self.vcube)
		self.cube.pack()
	def vrecprism(self):
		q1 = Label(self.frame, text="What is the height?")
		q2 = Label(self.frame, text="What is the width?")
		q3 = Label(self.frame, text="What is the length?")
		self.height = Entry(self.frame)
		self.width = Entry(self.frame)
		self.length = Entry(self.frame)

		q1.pack()
		self.height.pack()
		q2.pack()
		self.width.pack()
		q3.pack()
		self.length.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.vcalcrec)
		submit.pack()
	def vcalcrec(self):
		formula = Label(self.frame, text="Formula: height * width * length")
		formula.pack()
		height = float(self.height.get())
		width = float(self.width.get())
		length = float(self.length.get())
		result = height * width * length

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def vsphere(self):
		q1 = Label(self.frame, text="What is the radius?")
		self.radius = Entry(self.frame)

		q1.pack()
		self.radius.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.vcalcsphere)
		submit.pack()
	def vcalcsphere(self):
		formula = Label(self.frame, text="Formula: 4 * pi * radius^3 /3")
		formula.pack()
		radius = float(self.radius.get())
		result = 4 * pi * radius**3 / 3

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def vcone(self):
		q1 = Label(self.frame, text="What is the radius?")
		q2 = Label(self.frame, text="What is the height?")
		self.radius = Entry(self.frame)
		self.height = Entry(self.frame)

		q1.pack()
		self.radius.pack()
		q2.pack()
		self.height.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.vcalccone)
		submit.pack()
	def vcalccone(self):
		formula = Label(self.frame, text="Formula: base * height / 3")
		formula.pack()
		radius = float(self.radius.get())
		height = float(self.height.get())
		result = (pi * radius**2) * height / 3

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def vcylinder(self):
		q1 = Label(self.frame, text="What is the radius?")
		q2 = Label(self.frame, text="What is the height?")
		self.radius = Entry(self.frame)
		self.height = Entry(self.frame)

		q1.pack()
		self.radius.pack()
		q2.pack()
		self.height.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.vcalccylin)
		submit.pack()
	def vcalccylin(self):
		formula = Label(self.frame, text="Formula: pi * radius^2 *height")
		formula.pack()
		radius = float(self.radius.get())
		height = float(self.height.get())
		result = pi * radius**2 * height

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def vtriprism(self):
		q1 = Label(self.frame, text="What is the height?")
		q2 = Label(self.frame, text="What is the width?")
		q3 = Label(self.frame, text="What is the length?")
		self.height = Entry(self.frame)
		self.width = Entry(self.frame)
		self.length = Entry(self.frame)

		q1.pack()
		self.height.pack()
		q2.pack()
		self.width.pack()
		q3.pack()
		self.length.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.vcalctrip)
		submit.pack()
	def vcalctrip(self):
		formula = Label(self.frame, text="Formula: height * width /2 * length")
		formula.pack()
		height = float(self.height.get())
		width = float(self.width.get())
		length = float(self.length.get())
		result = height*width / 2 * length

		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def vpyramid(self):
		q1 = Label(self.frame, text="What is the height?")
		q2 = Label(self.frame, text="What is the width?")
		q3 = Label(self.frame, text="What is the length?")
		self.height = Entry(self.frame)
		self.width = Entry(self.frame)
		self.length = Entry(self.frame)


		q1.pack()
		self.height.pack()
		q2.pack()
		self.width.pack()
		q3.pack()
		self.length.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.vcalcpyramid)
		submit.pack()
	def vcalcpyramid(self):
		formula = Label(self.frame, text="Formula: length * width / 3 * height")
		formula.pack()
		height = float(self.height.get())
		width = float(self.width.get())
		length = float(self.length.get())
		result = length * width / 3 * height
		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
	def vcube(self):
		q1 = Label(self.frame, text="What is the length?")
		self.length = Entry(self.frame)

		q1.pack()
		self.length.pack()
		submit = Button(self.frame, text="Submit", fg = "blue", bg = "white", command = self.vcalccube)
		submit.pack()
	def vcalccube(self):
		formula = Label(self.frame, text="Formula: length^3")
		formula.pack()
		length = float(self.length.get())
		result = length**3
		res = Label(self.frame, text="Result/Answer: " + str(result))
		res.pack()
root = Tk()
allVolume=Volume(root);
root.mainloop()