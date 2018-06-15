import sys
import math
file = sys.stdin.read()
lines = file.split("\n")

def find_best_root(n):
	root = math.sqrt(n)
	if root == int(root):

		paper = n * root

	else:
		best = n - int(root)**2
		return root + best