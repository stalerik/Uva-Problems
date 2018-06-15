import sys
import math
file = sys.stdin.read()
lines = file.split("\n")

for e in lines:
	n = int(e)
	#print(math.ceil(math.log((n-1),2)))
	#print(n-1)
	print((n-1)+ math.ceil(math.log((n-1),2)))
	#print((n-1)*math.ceil(math.log((n-1),2)))