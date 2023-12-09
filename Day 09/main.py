# Naod Philemon
# 12/09/2023

def allZero(values):
	for val in values:
		if val != 0: return False
	return True

def part1(history):
	result = 0

	for hist in history:
		lasts = []
		while allZero(hist) == False:
			lasts.append(hist[-1])
			newHist = []
			for i in range(0,len(hist)-1):
				newHist.append(hist[i+1] - hist[i])
			hist = newHist
		
		lasts.append(0)
		new = [0]
		for i in range(len(lasts)-2, -1, -1):
			new.append(new[-1] + lasts[i])
		
		result += new[-1]

	return result

def part2(history):
	return part1([x[::-1] for x in history])

def main():
	file = open('./input.txt')

	history = []

	for line in file:
		history.append([int(x) for x in line.strip().split()])

	print('Part 1 -', part1(history))
	print('Part 2 -', part2(history))

main()