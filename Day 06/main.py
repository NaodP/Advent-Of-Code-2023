# Naod Philemon
# 12/06/2023

def part1(races):
	result = 1

	for time, distance in races:
		ways = 0

		for i in range(time):
			newDistance = i * (time-i)
			if newDistance > distance:
				ways += 1
		
		result *= ways

	return result

def part2(races):
	left = 0
	right = 0

	time = int("".join([str(x) for (x,y) in races]))
	distance = int("".join([str(y) for (x,y) in races]))

	for i in range(time):
		newDistance = i * (time-i)
		if newDistance > distance:
			left = i
			break

	for i in range(time, -1, -1):
		newDistance = i * (time-i)
		if newDistance > distance:
			right = i
			break
		
	result = (right - left) + 1
	return result

def main():
	file = open('./input.txt')

	time = [int(x) for x in file.readline().strip().split()[1:]]
	distance = [int(x) for x in file.readline().strip().split()[1:]]

	races = list(map(lambda x, y: (x, y), time, distance))
	print('Part 1 -', part1(races))
	print('Part 2 -', part2(races))

main()