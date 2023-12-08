# Naod Philemon
# 12/07/2023

import copy

def sort(hands):
	newHands = []
	cardsMap = {
		"2": "m",
		"3": "l",
		"4": "k",
		"5": "j",
		"6": "i",
		"7": "h",
		"8": "g",
		"9": "f",
		"T": "e",
		"J": "d",
		"Q": "c",
		"K": "b",
		"A": "a",
	}

	for hand in hands:
		mappedHand = "".join([cardsMap[let] for let in hand[0]])
		newHands.append((hand, mappedHand))
	
	sortedHands = [x[0] for x in sorted(newHands, key=lambda x: x[1])]

	return sortedHands

def isFive(hand):
	first = hand[0]

	for card in hand:
		if card != first: 
			return False
	
	return True

def isFour(hand):
	cards = {}

	for card in hand:
		if card not in cards: cards[card] = 0
		cards[card] += 1
	
	for card in cards:
		if cards[card] == 4: return True
	
	return False

def isFull(hand):
	cards = {}

	for card in hand:
		if card not in cards: cards[card] = 0
		cards[card] += 1
	
	cardsCopy = copy.deepcopy(cards)
	
	for card in cards:
		if cards[card] == 3: cardsCopy.pop(card)
		elif cards[card] == 2: cardsCopy.pop(card)
	
	if len(cardsCopy) != 0: return False
	return True

def isThree(hand):
	cards = {}

	for card in hand:
		if card not in cards: cards[card] = 0
		cards[card] += 1

	cardsCopy = copy.deepcopy(cards)

	for card in cards:
		if cards[card] == 3: cardsCopy.pop(card)
	
	if len(cardsCopy) != 2: return False
	return True

def isTwo(hand):
	cards = {}

	for card in hand:
		if card not in cards: cards[card] = 0
		cards[card] += 1

	if len(cards) == 3: return True
	return False

def isOne(hand):
	cards = {}

	for card in hand:
		if card not in cards: cards[card] = 0
		cards[card] += 1

	cardsCopy = copy.deepcopy(cards)

	for card in cards:
		if cards[card] == 2: cardsCopy.pop(card)

	if len(cards) == 4: return True
	return False

def part1(hands):
	result = 0

	five = []
	four = []
	full = []
	three = []
	two = []
	one = []
	high = []

	# Sort by type
	for hand in hands:
		if isFive(hand[0]): five.append(hand)
		elif isFour(hand[0]): four.append(hand)
		elif isFull(hand[0]): full.append(hand)
		elif isThree(hand[0]): three.append(hand)
		elif isTwo(hand[0]): two.append(hand)
		elif isOne(hand[0]): one.append(hand)
		else: high.append(hand)

	# Sort in type by strongest
	five = sort(five)
	four = sort(four)
	full = sort(full)
	three = sort(three)
	two = sort(two)
	one = sort(one)
	high = sort(high)

	total = five + four + full + three + two + one + high

	for i in range(len(total)-1, -1, -1):
		result += total[i][1] * ((len(total)-i))
	
	return result
	

def part2():
	pass

def main():
	file = open('./input.txt')
	hands = []

	for line in file:
		hand, bet = line.strip().split()
		hands.append((hand, int(bet)))

	print('Part 1 -', part1(hands))
	print('Part 2 -', part2())

main()

# [print("".join(sorted(x[0]))) for x in high]