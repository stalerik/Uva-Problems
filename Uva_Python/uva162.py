import sys

file = sys.stdin.read()

temp = file.split()

decks = []
for i in range(len(temp)):
	if i % 52 == 0:
		decks.append(temp[i-52:i])

decks.remove([])
face_cards = ["HJ", "HQ", "HK", "HA", "SJ", "SQ", "SK", "SA", "DJ", "DQ", "DK", "DA", "CJ", "CQ", "CK", "CA" ]


def player_switch(player, player1, dealer):
	if player == player1:
		return dealer
	else:
		return player1

def pop_card(player, s):
	card = player.pop(0)
	s.append(card)
	return card

def check_face(card):
	if card in face_cards:
		face = card[1]
		if face == "J":
			return 1
		elif face == "Q":
			return 2
		elif face == "K":
			return 3
		else: 
			return 4
	else:
		return 0

def face_winnner(player, num, s, p1, d):
	if not player or num == 0:
		return player

	else:
		current = pop_card(player, s)
		if check_face(current) == 0:
			face_winnner(player, num - 1, s, p1, d)
		else:
			face_winnner(player_switch(player, p1, d), check_face(current), s, p1, d)


def go_ham(d):
	player1 = []
	dealer = []
	stack = []

	flag = True
	for card in d:
		if flag:
			player1.append(card)
			flag = False
		else:
			dealer.append(card)
			flag = True


	current_player = player1
	while dealer and player1:
		print(player1)
		print(dealer)
		current_card = pop_card(current_player, stack)
		number = check_face(current_card)
		if number == 0:
			player_switch(current_player, player1, dealer)
		else:
			current_player = player_switch(face_winnner(current_player, number, stack, player1, dealer), player1, dealer)
			if dealer and player1:
				current_player.extend(stack)
				stack.clear()
			else: 
				pop_card(current_player, stack)
				break


	if current_player == player1:
		print(1, len(player1))

	else:
		print(2, len(dealer))


for deck in decks:
	go_ham(decks[0])








