import math
import sys
file = sys.stdin.read()
lines = file.split("\n")


test_case = int(lines[0])

def str_to_int(string):
	int_list = []
	for i in range(1, test_case + 1):
		for j in range(0, len(string[i])):
			if string[i][j] == " ":
				a = int(string[i][0:j])
				b = int(string[i][j+1:])
				int_list.append((a,b))
	return int_list

def calculate_sonars(int_list):
	temp_list = []
	for e in int_list:

		temp_a = e[0] - 2
		temp_b = e[1] - 2
		temp_list.append(int((math.ceil(temp_a/3.0) * math.ceil(temp_b/3.0))))

	return temp_list
		

def correct_output(wrong_output):
	string = ""
	for i in range(0, test_case):
		if not i == test_case - 1:
			string = string + str(wrong_output[i])
			string = string + "\n"
		if i == test_case - 1:
			string = string + str(wrong_output[i])
	return string

abc = str_to_int(lines)
aaa = calculate_sonars(abc)
result = correct_output(aaa)
print(result)