import sys
file = sys.stdin.read()
lines = file.split("\n")

for i in range(len(lines)+1):
	if lines[i] == "*":
		break
	else:
		if lines[i] == "Hajj":
			print("Case " + str(i+1) + ": " + "Hajj-e-Akbar")
		else:
			print("Case " + str(i+1) + ": " + "Hajj-e-Asghar")
