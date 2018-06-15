import sys
file = sys.stdin.read()
lines = file.split("\n")


first = True	


new_str = str()
i = 0

for line in lines:
	if line == "":
			break
	i = 0
	while i < len(line):
		if line[i] == '"':
			if first == True:
				line = line[:i] + '``' + line[i+1:]
				#new_str += '``'
				first = False
				i+=1
			elif first == False:
				line = line[:i] + "''" + line[i+1:]
				#new_str += "''"
				first = True
				i+=1
		i+=1
	print(line)




"""
while i < len(file):
	if file[i] == "":
		break
	if file[i] == '"':
		if first == True:
			file = file[:i] + '``' + file[i+1:]
			#new_str += '``'
			first = False
			i+=1
		elif first == False:
			file = file[:i] + "''" + file[i+1:]
			#new_str += "''"
			first = True
			i+=1
	else:
		#new_str += file[i]		
		i += 1
"""
#print(file)
#print(new_str)
