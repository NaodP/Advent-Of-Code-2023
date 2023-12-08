# Naod Philemon
# 12/08/2023

import math

def findSteps(connections, instructions, start):
	steps = 0
	current = start
	i = 0
	length = len(instructions)

	while current[-1] != 'Z':
		if instructions[i] == 'L':
			current = connections[current][0]
		
		elif instructions[i] == 'R':
			current = connections[current][1]

		i = (i+1) % length
		steps += 1

	return steps

def part1(instructions, elements):
	connections = {}

	for element in elements:
		connections[element[0]] = element[1]

	steps = 0
	current = 'AAA'
	i = 0
	length = len(instructions)

	while current != 'ZZZ':
		if instructions[i] == 'L':
			current = connections[current][0]
		
		elif instructions[i] == 'R':
			current = connections[current][1]

		i = (i+1) % length
		steps += 1

	return steps

def part2(instructions, elements):
	connections = {}
	current = []
	steps = 1

	for element in elements:
		connections[element[0]] = element[1]

		if element[0][-1] == 'A': current.append(element[0])

	for curr in current:
		steps = math.lcm(steps, findSteps(connections, instructions, curr))
		
	return steps

def main():
	file = open('./input.txt')
	elements = []

	instructions = file.readline().strip()
	file.readline()

	for line in file:
		element = line.strip().split(" = (")[0]
		connections = line.strip().split(" = (")[1].strip(")").split(", ")
		elements.append((element, connections))

	print('Part 1 -', part1(instructions, elements))
	print('Part 2 -', part2(instructions, elements))

main()