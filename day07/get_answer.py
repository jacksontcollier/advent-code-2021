#!/usr/bin/env python3

from day07 import *

positions = parse_input('test_input.txt')
test_answer = calc_min_fuel_required(positions, lambda x: x)
print("Test Input: %d" % test_answer)
positions = parse_input('input_day07.txt')
part_one_answer = calc_min_fuel_required(positions, lambda x: x)
print("Part One: %d" % part_one_answer)
part_two_answer = calc_min_fuel_required(positions, lambda x: (x * (x+1)) / 2)
print("Part Two: %d" % part_two_answer)

