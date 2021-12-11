#!/usr/bin/env python3

def parse_input(inputfile):
    fin = open(inputfile)
    grid = []

    for line in fin.readlines():
        row = [int(char) for char in line.strip()]
        grid.append(row)

    fin.close()
    return grid

