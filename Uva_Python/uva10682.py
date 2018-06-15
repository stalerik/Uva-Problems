import sys
import collections
file = sys.stdin.read()

lines = file.split("\n")

def add_to(dic, key, element):
	"""
	key: -string
	element: -tuple(string, int)
	"""
	if key in dic.keys():
		dic[key].append(element)
	else:
		dic[key] = [element]

	return dic

def get_chicos_way(n_roads, i_roads, destination):
	start, end = destination.split(" ")

	adjecency_dic = dict()
	flag_end = False
	flag_start = False
	for e in i_roads:
		temp = e.split(" ")
		city1 = temp[0]
		city2 = temp[1]
		if city2 == start or city1 == start:
			flag_start = True
		if city2 == end or city1 == end:
			flag_end = True
		speed = int(temp[2])
		add_to(adjecency_dic, city1, (city2, speed))
		add_to(adjecency_dic, city2, (city1, speed))

	
	if flag_end + flag_start != 2:
		return "No valid route."
	
	path = bfs(start, end, adjecency_dic)

	if path == False:
		return "No valid route."

	lista = [end]

	while start not in lista:
		lista.append(path[lista[-1]])

	path_string = ""
	lista.reverse()
	for e in lista:
		path_string += e +" "

	return path_string
	


def bfs(start, end, graph):
	#print(graph)
	prev = dict()
	current_speed = 0
	queue = collections.deque([start])
	seen = set([start])
	prev_speed = 0
	while queue:
		current = queue.popleft()
		
		for neighbour in graph[current]:
			if len(prev) == 0:
				if neighbour[0] == end:
						prev[end] = current
						return prev
				else:
					prev[neighbour[0]] = current
					seen.add(neighbour[0])
					queue.append(neighbour[0])
					prev_speed = neighbour[1]


			else:
				if neighbour[1] < prev_speed:
					pass

				elif neighbour[0] not in seen:

					if neighbour[1] > prev_speed:
						if neighbour[0] == end:
							prev[end] = current
							return prev

						else:
							prev[neighbour[0]] = current
							seen.add(neighbour[0])
							queue.append(neighbour[0])
							prev_speed = neighbour[1]

	return False







i = 0
while i < len(lines):
	roads = int(lines[i])
	i+=1
	roads_info = lines[i : i + roads]
	i += roads
	start_end = lines[i]
	i+=2

	print(get_chicos_way(roads, roads_info, start_end) + "\n")
