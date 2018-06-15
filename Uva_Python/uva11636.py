import sys
file = sys.stdin.read()
lines = file.split("\n")

def get_pasty_boii(n):
	pasty = 1
	counter = 0
	while pasty < n:
		counter += 1
		pasty *= 2
	return counter

a = 0
for number in lines:
	a += 1
	if int(number) < 0:
		break
	else:
		print("Case "+str(a)+":",get_pasty_boii(int(number)))