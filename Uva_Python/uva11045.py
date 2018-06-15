import sys
file = sys.stdin.read()
lines = file.split("\n")

cases = int(lines[0])
i = 1

def counta_dashirtas(peoples, shirters, the_list):
	the_new_list = []
	the_dict_demand = dict()
	the_dict_result = dict()
	for e in the_list:
		temp = e.split(" ")
		the_new_list.append((temp[0], temp[1]))
		#the_new_list.append(temp[1])


	size_list = ['XXL', 'XL', 'L', 'M', 'S', 'XS']
	each_shirt = shirters // 6
	"""
	for e in size_list:
			the_dict_demand[e] = 0
			the_dict_result[e] = 0
	
	for e in the_new_list:
		the_dict_demand[e[0]] += 1
		the_dict_demand[e[1]] += 1
	"""
	"""
	for pair in the_new_list:
		if the_dict_demand[pair[0]] > the_dict_demand[pair[1]]:
			if the_dict_result[pair[1]] == each_shirt:
				the_dict_result[pair[0]] += 1


			elif the_dict_result[pair[0]] == 1:
				the_dict_result[pair[1]] += 1

			else:
				the_dict_result[pair[1]] += 1

		elif the_dict_demand[pair[0]] < the_dict_demand[pair[1]]:
			if the_dict_result[pair[1]] == each_shirt:
				the_dict_result[pair[0]] += 1

			elif the_dict_result[pair[0]] == each_shirt:
				the_dict_result[pair[1]] += 1

			else:
				the_dict_result[pair[0]] += 1

		else:
			if the_dict_result[pair[1]] == each_shirt:
				the_dict_result[pair[0]] += 1

			elif the_dict_result[pair[0]] == each_shirt:
				the_dict_result[pair[1]] += 1

			else:
				the_dict_result[pair[1]] += 1

	flag = False
	for value in the_dict_result.values():

		if value >= each_shirt:
			flag == True

	if flag == True:
		return("YES")

	for i in range(2):
		for e in size_list:
			if the_dict_result[e] > each_shirt:
				#Try to switch the picked shirt
				for p in the_new_list:
					if e == p[0] and the_dict_result[p[1]] < each_shirt:
						the_dict_result[e] -= 1
						the_dict_result[p[1]] += 1

					elif e == p[1] and the_dict_result[p[0]] < each_shirt:
						the_dict_result[e] -= 1
						the_dict_result[p[0]] += 1

	flag = False
	for value in the_dict_result.values():

		if value >= each_shirt:
			flag == True

	if flag == True:
		return("YES")


	over = ""
	under = ""
	for e in size_list:
		if the_dict_result[e] > each_shirt:
			over = e

		if the_dict_result[e] < each_shirt and the_dict_demand[e] > the_dict_result[e]:
			under = e

	def find_correlation(start, end, lista, init):
		current = start
		if start == end:
			#the_dict_result[init] -= 1
			#the_dict_result[end] += 1
			#print(init, end)
			#print(the_dict_result)
			return True
		#for i in range(people):
		for e in size_list:
			if current == end:
				return True
			for p in lista:
				if e == p[0]:
					current = p[1]
					if current == end:
						return True
					lista.remove(p)
					find_correlation(current, end, lista,init)
				elif e == p[1]:
					current = p[0]
					if current == end:
						return True
					lista.remove(p)
					find_correlation(current, end, lista ,init)

	

	if over != "" and under != "":
		if find_correlation(over, under, the_new_list,over) == True:
			the_dict_result[under] +=1
			the_dict_result[over] -=1
			



	#print(the_dict_demand)
	#print(the_dict_result)
	print(each_shirt)
	print(the_new_list)
	print(the_dict_demand)
	print(the_dict_result)

	for value in the_dict_result.values():
		if value > each_shirt:
			return("NO")

	return "YES"
	"""
	def recursive(seq):
		if not seq:
			return []

		else:
			return [seq[0][0]] + recursive(seq[1:])

	a = recursive(the_new_list)
	print(a)


	#print(the_new_list)









b = 0
while i <  2:
	temp = lines[i].split(" ")
	shirts = int(temp[0])
	people = int(temp[1])
	#b+=1
	print(b)
	print(counta_dashirtas(people, shirts,lines[i+1:people+i+1]))
	i += people+1

