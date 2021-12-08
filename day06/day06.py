#!/usr/bin/env python3

def read_input_file(inputfile):
    fin = open(inputfile)
    lanternfish = [int(fish) for fish in fin.readline().strip().split(',')]
    fin.close()
    return lanternfish

def populate_lanternfish(lanternfish, num_days):
    for day in range(num_days):
        new_fish = []
        for i in range(len(lanternfish)):
            if lanternfish[i] == 0:
                lanternfish[i] = 6
                new_fish.append(8)
            else:
                lanternfish[i] -= 1
        lanternfish = lanternfish + new_fish

    return lanternfish

lanternfish = read_input_file('test_input.txt')
lanternfish = populate_lanternfish(lanternfish, 18)
print('Test input solution: %d' % len(lanternfish))
lanternfish = read_input_file('input_day06.txt')
lanternfish = populate_lanternfish(lanternfish, 80)
print('Part one solution: %d' % len(lanternfish))

