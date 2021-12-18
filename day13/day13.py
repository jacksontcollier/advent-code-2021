#!/usr/bin/env python3

def parse_input(inputfile):
    fin = open(inputfile)
    positions = []
    fold_positions = []

    for line in fin:
        if 'fold' in line:
            fw, sw, tw = line.strip().split()
            axis, fold_position = tw.split('=')
            fold_positions.append((axis, int(fold_position)))
        elif ',' in line:
            x, y = line.strip().split(',')
            positions.append((int(x), int(y)))

    fin.close()

    return (positions, fold_positions)

