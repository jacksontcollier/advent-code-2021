#!/usr/bin/env python3

from height_map import *
from day09 import *

test_input_heights = parse_input('test_input.txt')
height_map = HeightMap(test_input_heights)
risk = height_map.get_low_point_risk()
print("Part One (Test Input): %d" % risk)
input_heights = parse_input('input_day09.txt')
height_map = HeightMap(input_heights)
risk = height_map.get_low_point_risk()
print("Part One: %d" % risk)
height_map = HeightMap(test_input_heights)
basin_product = height_map.get_largest_basins_product()
print("Part Two (Test Input): %d" % basin_product)
height_map = HeightMap(input_heights)
basin_product = height_map.get_largest_basins_product()
print("Part Two: %d" % basin_product)
