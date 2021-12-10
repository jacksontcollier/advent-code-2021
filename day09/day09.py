#!/usr/bin/env python3

def parse_input(inputfile):
    fin = open(inputfile)
    height_map_matrix = []

    for line in fin.readlines():
        heights_str = line.strip()
        heights = []
        for height in heights_str:
            heights.append(int(height))
        height_map_matrix.append(heights)

    return height_map_matrix

