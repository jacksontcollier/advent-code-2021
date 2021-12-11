#!/usr/bin/env python3

from day11 import parse_input
from octopus_grid import OctopusGrid

test_input = parse_input('test_input.txt')
test_octopus_g = OctopusGrid(test_input)
test_octopus_g.simulate_nsteps(100)
print("Part One (test input): %d" % test_octopus_g.get_num_flashes())
input_grid = parse_input('input_day11.txt')
octopus_g = OctopusGrid(input_grid)
octopus_g.simulate_nsteps(100)
print("Part One: %d" % octopus_g.get_num_flashes())
test_input = parse_input('test_input.txt')
test_octopus_g = OctopusGrid(test_input)
test_octopus_g.synchronize()
print("Part Two (Test Input): %d" % test_octopus_g.get_synchronization_step())
input_grid = parse_input('input_day11.txt')
octopus_g = OctopusGrid(input_grid)
octopus_g.synchronize()
print("Part Two: %d" % octopus_g.get_synchronization_step())
