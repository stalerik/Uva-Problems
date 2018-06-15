import  sys
file = sys.stdin.read()
lines = file.split("\n")

def hangman_yoo(answer, guess):
	stroke = 0
	new_answer = answer
	new_guess = ""
	for e in guess:
		if e not in new_guess:
			stroke += 1
		new_guess += e

		if e in new_answer:
			new_answer = new_answer.replace(e,"")
			stroke -= 1

		#print(new_answer, new_guess, stroke)

		if stroke == 7:
			return "You lose."

		if new_answer == "":
			return "You win."

	#if stroke >= 7:
		#return "You lose."

	else:
		return "You chickened out."
i = 0
while i < len(lines):
	if i % 3 == 0:
		if lines[i] == '-1':
			break
		else:
			print("Round", lines[i])
			i+=1
	else:

		print(hangman_yoo(lines[i],lines[i+1]))
		i+=2