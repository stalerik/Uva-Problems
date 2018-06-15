import sys
file = sys.stdin.read()
lines = file.split("\n")

cases = int(lines[0])

def decrypt(secret):
	int_secret = int(secret)
	if int_secret == 1 or int_secret == 4 or int_secret == 78:
		print("+")
	elif secret[-2:] == '35':
		print("-")
	elif secret[0] == '9' and secret[-1] == '4':
		print("*")
	elif secret[:3] == '190':
		print("?") 
	else:
		print("?")


for i in range(1,cases+1):
	#print(lines[i])
	decrypt(lines[i])