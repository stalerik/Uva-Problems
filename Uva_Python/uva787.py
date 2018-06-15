import sys
import itertools
file = sys.stdin.read()

numbers = file.split()
numbers = list(map(int, numbers))
sequences = []

i = 0
k = 0
for n in numbers:
	if n == -999999:
		sequences.append(numbers[k:i])
		k = i + 1
		i += 1
	else:
		i += 1



def get_sublists(seq):
	temp = []
	for i in range(len(seq)+1):
		for y in range(i, len(seq)):
			temp.append(seq[i:y+1])

	return temp

def multiply_shit(seq):
	a = 1
	for n in seq:
		a *= n
	return a


def da_thing_goes_skkrrrt(seq):
	sub_lists = get_sublists(seq)
	list_of_products = []
	if len(seq) == 1:
		return seq[0]
	else:
		for e in sub_lists:
			list_of_products.append(multiply_shit(e))

	return max(list_of_products)


for e in sequences:
	print(da_thing_goes_skkrrrt(e))




