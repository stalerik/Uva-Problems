import sys

file = sys.stdin.read()

lines = file.split("\n")

for i in range (len(lines)):
	if lines[i] == "*":
		shapes = lines[:i]
		points = lines[i+1:]



circles = []
rects = []

shape_dict = dict()

for i in range(len(shapes)):
	shape_dict[shapes[i]] = i+1
	if shapes[i][0] == "r":
		rects.append(shapes[i])
	else:
		circles.append(shapes[i])



def circle_check(point, n):
	flag = False
	p = point.split()
	p_x , p_y= float(p[0]), float(p[1])
	for c in circles:
		temp = c.split()
		x = float(temp[1])
		y = float(temp[2])
		r = float(temp[3])

		calc = (x - p_x)**2 + (p_y -y)**2
		if r**2 > calc:
			print("Point", n, "is contained in figure",  shape_dict[c])
			flag = True

	return flag


def rect_check(point, n):
	flag = False
	p = point.split()
	p_x , p_y= float(p[0]), float(p[1])
	for r in rects:
		temp = r.split()
		x_u = float(temp[1])
		y_u = float(temp[2])
		x_d = float(temp[3])
		y_d = float(temp[4])

		if x_u < p_x and x_d > p_x and y_u > p_y and y_d < p_y:
			print("Point", n, "is contained in figure", shape_dict[r])
			flag = True

	return flag

for i in range(len(points)):
	if points[i] == "9999.9 9999.9":
		break
	b = rect_check(points[i], i+1)
	a = circle_check(points[i], i+1)
	
	if not a and not b:
		print("Point",i+1, "is not contained in any figure")


