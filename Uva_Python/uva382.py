import sys
file = sys.stdin.read()
numbers = file.split()


def perfect_number(n):
	if n == 1:
		return "DEFICIENT"
	res = 0
	halfish = ((n//2)+1)

	for i in range(1, halfish):
		if n/i == n//i:
			res += i
		
	if res < n:
		return "DEFICIENT"
	elif res == n:
		return "PERFECT"
	else:
		return "ABUNDANT"
		

print("PERFECTION OUTPUT")
for e in numbers:
	if e == '0':
		print("END OF OUTPUT")
	else:
		res = perfect_number(int(e))
		string = "%5s  %s" % (e, res)
		print(string)