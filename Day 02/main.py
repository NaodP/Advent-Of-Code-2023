# Naod Philemon
# 12/02/2023

def part1(games):
	max_red = 12
	max_green = 13
	max_blue = 14

	result = 0

	for game in games:

		for selection in game[1]:
			red = 0
			green = 0
			blue = 0
			invalid = False

			draws = selection.split(", ")
			for draw in draws:
				num, color = draw.strip().split(" ")
				
				if color == "red":
					red += int(num)
				
				if color == "green":
					green += int(num) 
				
				if color == "blue":
					blue += int(num)
		
			if red > max_red: invalid = True
			if green > max_green: invalid = True
			if blue > max_blue: invalid = True

			if invalid: break

		if not invalid:
			result += int(game[0])

	return result

def part2(games):
	result = 0

	for game in games:
		max_red = 0
		max_green = 0
		max_blue = 0

		for selection in game[1]:
			draws = selection.split(", ")
			for draw in draws:
				num, color = draw.strip().split(" ")
				
				if color == "red":
					max_red = max(max_red, int(num))
				
				if color == "green":
					max_green = max(max_green, int(num))
				
				if color == "blue":
					max_blue = max(max_blue, int(num))
				
		result += (max_red*max_green*max_blue)

	return result

def main():
	file = open('./input.txt')

	games = []

	for line in file:
		game_name, game_values = line.split(":")
		id = game_name.split(" ")[1]
		values = game_values.split(";")

		games.append((id, values))

	print('Part 1 -', part1(games))
	print('Part 2 -', part2(games))

main()