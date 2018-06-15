import sys
import string
file = sys.stdin.read()
lines = file.split("\n")

def count_chars(text):
	dic = dict()
	big = ""
	chars = []
	for e in text:
		if e in string.ascii_lowercase or e in string.ascii_uppercase:
			if e in dic.keys():
				dic[e] += 1

			else:
				dic[e] = 1
				chars.append(e)

	biggest = sorted(dic.values())[-1]
	for char in chars:
		if dic[char] == biggest:
			big += char

	return big, biggest


for line in lines:
	if line == "":
		break
	letters, number = count_chars(line)
	print("".join(sorted(letters)), number)
