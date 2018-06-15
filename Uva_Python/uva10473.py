import sys
file = sys.stdin.read()
lines = file.split("\n")

for n in lines:
	if n[:2] == '0x':
		print(int(n, 16))

	elif int(n) < 0:
		break

	else:
		a = hex(int(n))
		a = a[:2] + a[2:].upper()
		print(a)