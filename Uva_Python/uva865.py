import sys 
file = sys.stdin.read()
lines = file.split("\n")

cases = int(lines[0])

def substitute(text):
	plaintext = text[0]
	subs = text[1]

	subs_dict = dict()

	for i in range(len(plaintext)):
		subs_dict[plaintext[i]] = subs[i]

	print(subs_dict)

i = 0
list_of_text = []
while i < len(lines):
	if lines[i] == "":
		list_of_text.append(i)
	i += 1
