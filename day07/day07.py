#!/usr/bin/env python3

def parse_input(inputfile):
    fin = open(inputfile)
    line = fin.readline()
    positions = [int(position) for position in line.strip().split(',')]
    fin.close()
    return positions

def calc_min_fuel_required(positions, fuel_cost_func):
    min_pos = min(positions)
    max_pos = max(positions)
    min_fuel_required = 0
    min_fuel_set = False

    for target_pos in range(min_pos, max_pos+1):
        fuel_required = 0
        for pos in positions:
            fuel_required += fuel_cost_func(abs(pos - target_pos))
        if not min_fuel_set:
            min_fuel_required = fuel_required
            min_fuel_set = True
        else:
            min_fuel_required = min(min_fuel_required, fuel_required)

    return min_fuel_required

