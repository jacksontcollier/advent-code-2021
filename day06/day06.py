#!/usr/bin/env python3

def read_input_file(inputfile):
    fin = open(inputfile)
    lanternfish = [int(fish) for fish in fin.readline().strip().split(',')]
    fin.close()
    return lanternfish

def get_lanternfish_population(lanternfish, num_days):
    lanternfish_states = [0] * 9
    for fish in lanternfish:
        lanternfish_states[fish] += 1

    for day in range(num_days):
        new_lanternfish = lanternfish_states[0]
        for i in range(0, len(lanternfish_states)-1):
            lanternfish_states[i] = lanternfish_states[i+1]
        lanternfish_states[8] = new_lanternfish
        lanternfish_states[6] += new_lanternfish

    return sum(lanternfish_states)

lanternfish = read_input_file('test_input.txt')
num_lanternfish = get_lanternfish_population(lanternfish, 18)
print('Test input solution: %d' % num_lanternfish)
lanternfish = read_input_file('input_day06.txt')
num_lanternfish = get_lanternfish_population(lanternfish, 80)
print('Part one solution: %d' % num_lanternfish)
num_lanternfish = get_lanternfish_population(lanternfish, 256)
print('Part two solution: %d' % num_lanternfish)

