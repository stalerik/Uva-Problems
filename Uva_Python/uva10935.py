import sys
file = sys.stdin.read()
lines = file.split("\n")

def poopoo(num):
	temp = [i for i in range(1, int(num)+1)]
	disc = []

	while len(temp) > 1:

		disc.append(temp.pop(0))
		temp.append(temp.pop(0))

	string = ", ".join(map(str, disc))
	if string == "":
		print("Discarded cards:")
	else:
		print("Discarded cards:",  string)
	print("Remaining card:", temp[0])

for n in lines:
	if n == '0':
		break
	poopoo(n)