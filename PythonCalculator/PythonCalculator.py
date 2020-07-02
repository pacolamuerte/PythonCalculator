#define the start and print what the program is
def start():
	print("Area Calculator in Python")
	print("="*25)
#start of the while loop. Makes it so we don't get kicked out if wrong input
while True:
	_input_ = input("Enter 'C' for circle or 'T' for triangle or 'R' for Rectangle: ")
#formulas for the different area calculations
	if _input_ == 'C':
		radius = float(input("what is the radius of the circle in meters (m)?: "))
		area_c = 2 * 3.14159 * radius
		print("The area of the circle is " + str(area_c) + " m2)")

	elif _input_ == 'T':
		base = float(input("what is the base measurement (m)?: "))
		height = float(input("what is the height measuerment (m)?: "))
		area_t = 0.5 * base * height
		print("The area of the triangle is " + str(area_t) + " m2")

	elif _input_ == 'R':
		length = float(input("what is the length measurement (m)?: "))
		width = float(input("what is the width measuerment (m)?: "))
		area_r = length * width
		print("The area of the rectangle is " + str(area_r) + " m2")
	else:
		print("Sorry, that was an invalid command!")