# Naod Philemon
# 12/01/2023

def findFirst(val):
	for let in val:
		if let.isdigit(): 
			return let
		
	return

def findLast(val):
	for i in range(len(val)-1, -1, -1):
		if val[i].isdigit(): 
			return val[i]
		
	return

def part1(values):
	sum = 0

	for val in values:
		sum += int(findFirst(val) + findLast(val))

	return sum

def part2():
	pass

def main():
	file = open('./input.txt')
	values = []

	for line in file:
		values.append(line)

	print('Part 1 -', part1(values))
	print('Part 2 -', part2())

main()