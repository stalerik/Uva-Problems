import sys
file = sys.stdin.read()

numbers = file.split()

dic = {}
order_list = []
for n in numbers:
	if n in dic.keys():
		dic[n] += 1
	else:
		dic[n] = 1
		order_list.append(n)

for e in order_list:
	print(e, dic[e])