#!/usr/bin/env python3

def parse_input(inputfile):
    fin = open(inputfile)
    edge_list = []

    for line in fin:
        start, end = line.strip().split('-')
        edge_list.append((start, end))

    fin.close()
    return edge_list

