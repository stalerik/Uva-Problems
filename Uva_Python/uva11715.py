import sys
import math
from decimal import *

file = sys.stdin.read()
lines = file.split("\n")

getcontext().prec = 20


def get_s_a(u,v,t):
	s = float(((v+u)/2)*t)
	a = ((v-u)/t)

	s = Decimal(s).quantize(Decimal('0.000'))
	a = Decimal(a).quantize(Decimal('0.000'))
	return s, a

def get_s_t(u,v,a):
	t = ((v-u)/a)
	s = (((v+u)/2)*t)
	
	t = Decimal(t).quantize(Decimal('0.000'))
	s = Decimal(s).quantize(Decimal('0.000'))

	return s, t

def get_v_t(u,a,s):
	v = math.sqrt(2*a*s + u**2)
	t = ((v-u)/a)
	
	v = Decimal(v).quantize(Decimal('0.000'))
	t = Decimal(t).quantize(Decimal('0.000'))

	return v,t

def get_u_t(v,a,s):
	u = math.sqrt(v**2 - 2*a*s)
	t = ((v-u)/a)
	
	u = Decimal(u).quantize(Decimal('0.000'))
	t = Decimal(t).quantize(Decimal('0.000'))
	return u,t

get_s_a(10, 5, 2)
get_s_a(5, 10, 2)
get_s_t(10, 11, 2)
get_v_t(5, 1, 6)
get_u_t(5, -1, 6)


i = 1
for e in lines:
	if e == '0':
		break
	else:
		#da_string = "Case " + str(i) + ":"

		temp = e.split(" ")
		if e[0] == '1':
			a, b = get_s_a(float(temp[1]), float(temp[2]), float(temp[3]))
		elif e[0] == '2':
			a, b = get_s_t(float(temp[1]), float(temp[2]), float(temp[3]))
		elif e[0] == '3':
			a, b = get_v_t(float(temp[1]), float(temp[2]), float(temp[3]))
		else:
			a ,b = get_u_t(float(temp[1]), float(temp[2]), float(temp[3]))

		print("Case " + str(i) + ":", a, b)

		i+=1
		

