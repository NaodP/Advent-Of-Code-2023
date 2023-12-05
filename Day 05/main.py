# Naod Philemon
# 12/05/2023

import sys

def part1(seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTempertature, temperatureToHumidity, humidityToLocation):
	result = sys.maxsize

	for seed in seeds:
		mapped = seed
		for destination, source, length in seedToSoil:
			if mapped >= source and mapped <= source+length:
				mapped = destination + (mapped - source)
				break
		
		for destination, source, length in soilToFertilizer:
			if mapped >= source and mapped <= source+length:
				mapped = destination + (mapped - source)
				break
		
		for destination, source, length in fertilizerToWater:
			if mapped >= source and mapped <= source+length:
				mapped = destination + (mapped - source)
				break
		
		for destination, source, length in waterToLight:
			if mapped >= source and mapped <= source+length:
				mapped = destination + (mapped - source)
				break
		
		for destination, source, length in lightToTempertature:
			if mapped >= source and mapped <= source+length:
				mapped = destination + (mapped - source)
				break
		
		for destination, source, length in temperatureToHumidity:
			if mapped >= source and mapped <= source+length:
				mapped = destination + (mapped - source)
				break
		
		for destination, source, length in humidityToLocation:
			if mapped >= source and mapped <= source+length:
				mapped = destination + (mapped - source)
				break

		result = min(result, mapped)

	return result

def part2(seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTempertature, temperatureToHumidity, humidityToLocation):
	pass


def main():
	file = open('./input.txt')

	seeds = [int(x) for x in file.readline().strip().split(" ")[1:]]
	seedToSoil = []
	soilToFertilizer = []
	fertilizerToWater = []
	waterToLight = []
	lightToTempertature = []
	temperatureToHumidity = []
	humidityToLocation = []

	while True:
		line = file.readline()
		if not line: break
		line = line.strip()

		if line == "seed-to-soil map:": 
			while True:
				line = file.readline().strip()
				if line == '': break
				destination, source, length = line.split(" ")
				seedToSoil.append((int(destination), int(source), int(length)))
		elif line == "soil-to-fertilizer map:": 
			while True:
				line = file.readline().strip()
				if line == '': break
				destination, source, length = line.split(" ")
				soilToFertilizer.append((int(destination), int(source), int(length)))
		elif line == "fertilizer-to-water map:":
			while True:
				line = file.readline().strip()
				if line == '': break
				destination, source, length = line.split(" ")
				fertilizerToWater.append((int(destination), int(source), int(length)))
		elif line == "water-to-light map:":
			while True:
				line = file.readline().strip()
				if line == '': break
				destination, source, length = line.split(" ")
				waterToLight.append((int(destination), int(source), int(length)))
		elif line == "light-to-temperature map:":
			while True:
				line = file.readline().strip()
				if line == '': break
				destination, source, length = line.split(" ")
				lightToTempertature.append((int(destination), int(source), int(length)))
		elif line == "temperature-to-humidity map:":
			while True:
				line = file.readline().strip()
				if line == '': break
				destination, source, length = line.split(" ")
				temperatureToHumidity.append((int(destination), int(source), int(length)))
		elif line == "humidity-to-location map:":
			while True:
				line = file.readline().strip()
				if line == '': break
				destination, source, length = line.split(" ")
				humidityToLocation.append((int(destination), int(source), int(length)))

	print('Part 1 -', part1(seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTempertature, temperatureToHumidity, humidityToLocation))
	print('Part 2 -', part2(seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTempertature, temperatureToHumidity, humidityToLocation))

main()