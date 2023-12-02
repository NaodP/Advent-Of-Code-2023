# Naod Philemon
# 12/01/2023

def part1(values):
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

	sum = 0

	for val in values:
		sum += int(findFirst(val) + findLast(val))

	return sum

def part2(values):
	def findFirst(value):
		tempValue = ""
		found = False
		val = 0

		for let in value:
			if let.isdigit(): 
				return let
			
			tempValue += let

			for index, num in enumerate(word_nums):
				if num in tempValue:
					val = index + 1
					found = True
					break
			
			if found: 
				break
		
		return str(val)

	def findLast(value):
		tempValue = ""
		found = False
		val = 0

		for i in range(len(value)-1, -1, -1):
			if value[i].isdigit(): 
				return value[i]
			
			tempValue = value[i] + tempValue

			for index, num in enumerate(word_nums):
				if num in tempValue:
					val = index + 1
					found = True
					break
			
			if found: 
				break
		
		return str(val)

	word_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	result = 0

	for value in values:
		result += int(findFirst(value) + findLast(value))

	return result

def main():
	file = open('./input.txt')
	values = []

	for line in file:
		values.append(line)

	print('Part 1 -', part1(values))
	print('Part 2 -', part2(values))

main()