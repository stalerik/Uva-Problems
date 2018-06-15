import sys
file = sys.stdin.read()
lines = file.split("\n")

pairs = []

for e in lines:
	temp = e.split()
	pairs = pairs + [temp]



def collatz(start, limit):
	terms = 0
	while start <= limit:
		if start == 1:
			terms += 1
			return terms
		elif start % 2 == 0:
			start = start/2
		else:
			start = (start*3) +1
		terms += 1

	return terms

i = 0
while i < len(pairs):
	a = int(pairs[i][0])
	b = int(pairs[i][1])
	if a < 0 and b < 0:
		break
	else:
		term = collatz(a, b)
		print("Case %s: A = %s, limit = %s, number of terms = %s" % ((i+1), a, b, term))
		i += 1

