import sys
import itertools
file = sys.stdin.read()
lines = file.split("\n")

			

def pallindrome_checker(b_string):
	if len(b_string) == 1:
		return b_string
	if len(b_string) % 2 == 0:
		left = b_string[len(b_string)//2:]
		right = b_string[:len(b_string)//2]
		if left == right[::-1]:
			return b_string
		else:
			return False
	else:
		right = b_string[int(len(b_string)//2) +1:]
		left = b_string[:len(b_string)//2]
		if left == right[::-1]:
			return b_string
		else:
			return False

def pallindromer(a_string):
	pali_list = []
	for i in range(len(a_string)+1):
		for j in range(len(a_string)+1):
			if a_string[i:j] != "":
				
				if pallindrome_checker(a_string[i:j]) != False:
					pali_list.append(pallindrome_checker(a_string[i:j]))
				
	return str(len(set(pali_list)))	


i= 0
while i < len(lines):
	if lines[i] == "":
		i+=1
	else:
		print("The string " + "'" + lines[i] + "'" + " contains " + pallindromer(lines[i]) + " palindromes.")
		i += 1

