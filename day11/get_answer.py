#!/usr/bin/env python3

from day11 import parse_input
from octopus_grid import OctopusGrid

test_input = parse_input('test_input.txt')
octopus_g = OctopusGrid(test_input)
octopus_g.simulate_nsteps(100)
print("Part One (test input): %d" % octopus_g.get_num_flashes())
input_grid = parse_input('input_day11.txt')
octopus_g = OctopusGrid(input_grid)
octopus_g.simulate_nsteps(100)
print("Part One: %d" % octopus_g.get_num_flashes())
