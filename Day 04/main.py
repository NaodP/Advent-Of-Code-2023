# Naod Philemon
# 12/04/2023

def part1(cards):
	values = 0

	for card in cards:
		matches = 0
		winning = set(card.split(" | ")[0].split(": ")[1].split(" "))
		mine = card.split(" | ")[1].split(" ")

		for number in mine:
			if number != '' and number in winning:
				matches = matches*2 if matches != 0 else 1
		
		values += matches

	return values

def part2(cards):

	copies = {}
	totalCards = len(cards)
	
	for card in cards:
		matches = 0
		
		cardNum = int(card.split(": ")[0][4:].strip())
		winning = set(card.split(" | ")[0].split(": ")[1].split(" "))
		mine = card.split(" | ")[1].split(" ")

		for number in mine:
			if number != '' and number in winning:
				matches += 1
		
		for i in range(1, matches+1):
			nextCard = cardNum+i
			if nextCard not in copies: copies[nextCard] = 0
			if cardNum in copies: copies[nextCard] += copies[cardNum]
			copies[nextCard] += 1

	for copy in copies:
		totalCards += copies[copy]

	return totalCards

def main():
	file = open('./input.txt')
	cards = []

	for line in file:
		cards.append(line.strip())

	print('Part 1 -', part1(cards))
	print('Part 2 -', part2(cards))

main()