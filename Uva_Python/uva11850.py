import sys
file = sys.stdin.read()
lines = file.split("\n")
for i in range(len(lines) -1):
	lines[i] = int(lines[i])


def is_possiblos(places):
	
	a = sorted(places[1:])
	res = ""
	if not a:
		return False
	if (1422 - a[-1])*2 > 200:
		return ("IMPOSSIBLE")
	else:
		for i in range(1,len(a)):
			if (a[i] - a[i-1]) > 200:
				return ("IMPOSSIBLE")
			else:
				res = "POSSIBLE"
		return res


current = lines[0] +1
counter = 0
"""
#print(counter, current)
print(is_possiblos(lines[counter:current]))
counter = current
current += lines[counter] +1
print(is_possiblos(lines[counter:current]))
#print(counter, current)
counter = current
current += lines[counter] +1
#print(counter, current)
print(is_possiblos(lines[counter:current]))

counter = current
current += lines[counter] +1
#print(counter, current)
print(is_possiblos(lines[counter:current]))

counter = current
current += lines[counter] +1
#print(counter, current)
print(is_possiblos(lines[counter:current]))
"""
while True:
	if is_possiblos(lines[counter:current]) == False:
		break;
	print(is_possiblos(lines[counter:current]))
	counter = current
	current += lines[counter] +1

	