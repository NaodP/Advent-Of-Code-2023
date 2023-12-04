# Naod Philemon
# 12/03/2023

def part1(grid):
	def findDigit(i, j):
		if grid[i][j].isdigit() and (i, j) not in seen:
			# Digit is found
			seen.add((i, j))
			number = grid[i][j]

			# Check left
			temp_j = j-1
			while temp_j > -1 and grid[i][temp_j].isdigit():
				seen.add((i, temp_j))
				number = grid[i][temp_j] + number
				temp_j -= 1

			# Check right
			temp_j = j+1
			while temp_j < len(grid[0]) and grid[i][temp_j].isdigit():
				seen.add((i, temp_j))
				number += grid[i][temp_j]
				temp_j += 1
			
			return number

		return None
	
	seen = set() # Consists of tuples of (x,y) which are points that we have already checked
	numbers = []
	
	# Go through grid and find symbols
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			point = grid[i][j]

			if not point.isdigit() and point != '.':
				# Check all points around symbol for digit
				neighbors = [
					(i-1, j-1),
					(i-1, j),
					(i-1, j+1),
					(i, j-1),
					(i, j+1),
					(i+1, j-1),
					(i+1, j),
					(i+1, j+1)
				]

				for neighbor in neighbors:
					if neighbor[0] > -1 and neighbor[0] < len(grid) and neighbor[1] > -1 and neighbor[1] < len(grid[0]):
						number = findDigit(neighbor[0], neighbor[1])
						if number is not None:
							# Add whole number to the "numbers" list
							numbers.append(number)

	# Return sum of all numbers
	return sum([int(x) for x in numbers])

def part2(grid):
	def findDigit(i, j):
		if grid[i][j].isdigit() and (i, j) not in seen:
			# Digit is found
			seen.add((i, j))
			number = grid[i][j]

			# Check left
			temp_j = j-1
			while temp_j > -1 and grid[i][temp_j].isdigit():
				seen.add((i, temp_j))
				number = grid[i][temp_j] + number
				temp_j -= 1

			# Check right
			temp_j = j+1
			while temp_j < len(grid[0]) and grid[i][temp_j].isdigit():
				seen.add((i, temp_j))
				number += grid[i][temp_j]
				temp_j += 1
			
			return number

		return None
	
	seen = set() # Consists of tuples of (x,y) which are points that we have already checked
	numbers = []
	gearRatios = 0
	
	# Go through grid and find symbols
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			point = grid[i][j]

			if not point.isdigit() and point != '.':
				# Check all points around symbol for digit
				neighbors = [
					(i-1, j-1),
					(i-1, j),
					(i-1, j+1),
					(i, j-1),
					(i, j+1),
					(i+1, j-1),
					(i+1, j),
					(i+1, j+1)
				]

				numGears = 0
				for neighbor in neighbors:
					if neighbor[0] > -1 and neighbor[0] < len(grid) and neighbor[1] > -1 and neighbor[1] < len(grid[0]):
						number = findDigit(neighbor[0], neighbor[1])
						if number is not None:
							# Add whole number to the "numbers" list
							numbers.append(number)
							numGears += 1
				
				if numGears == 2 and point == '*':
					gearRatios += int(numbers[-1]) * int(numbers[-2])

	# Return sum of all numbers
	return gearRatios

def main():
	file = open('./input.txt')
	grid = []

	for line in file:
		grid.append(line.strip())

	print('Part 1 -', part1(grid))
	print('Part 2 -', part2(grid))

main()