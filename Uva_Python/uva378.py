import sys
file = sys.stdin.read()
lines = file.split("\n")
from decimal import *


def intersect(p1, p2, p3, p4):
	k1, m1 = create_eq(p1, p2)
	k2, m2 = create_eq(p3, p4)


	if k1 == "Special":
		if k2 == "Special":
			if m1 == m2:
				return "LINE"
			else:
				return "NONE"
		else:
			intersect_x = m1
			intersect_y = (k2*intersect_x) + m2

			return "POINT " + str(Decimal(intersect_x).quantize(Decimal('0.00'))) +" "+ str(Decimal(intersect_y).quantize(Decimal('0.00')))


	elif k2 == "Special":
		if k1 == "Special":
			if m1 == m2:
				return "LINE"
			else:
				return "NONE"
		else:
			the_x = m2
			intersect_y = (k1*intersect_x) + m1

			return "POINT " + str(Decimal(intersect_x).quantize(Decimal('0.00'))) +" "+ str(Decimal(intersect_y).quantize(Decimal('0.00')))


	else:
		if k1 == k2:
			if m1 == m2:
				return "LINE"
			else:
				return "NONE"

		else:
			intersect_x = ((m2-m1)/(k1-k2))
			intersect_y = (k1*intersect_x) + m1

			return "POINT " + str(Decimal(intersect_x).quantize(Decimal('0.00'))) +" "+ str(Decimal(intersect_y).quantize(Decimal('0.00')))


def create_eq(point_s, point_e):
	x1 = int(point_s[0])
	y1 = int(point_s[1])
	x2 = int(point_e[0])
	y2 = int(point_e[1])

	if x2 - x1 == 0:
		return "Special", x1

	else:
		k = ((y2 - y1)/(x2 -x1))

		m = y1 - (k * x1)

		return k, m


i = 1
print("INTERSECTING LINES OUTPUT")
while i < int(lines[0]) +1:
	temp = lines[i].split(" ")
	p1 = temp[0], temp[1]
	p2 = temp[2], temp[3]
	p3 = temp[4], temp[5]
	p4 = temp[6], temp[7]
	print(intersect(p1, p2, p3, p4))
	i += 1



print("END OF OUTPUT")
#intersect((0,0), (4,4), (0,4), (4,0))

