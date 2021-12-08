#!/usr/bin/env python3

from hydro_vent import *

def parse_input(inputfile):
    fin = open(inputfile)
    line_endpoints = []

    for line in fin:
        halves = line.rstrip().split('->')
        x1, y1 = [int(num) for num in halves[0].rstrip().split(',')]
        x2, y2 = [int(num) for num in halves[1].rstrip().split(',')]
        endpoints = ((x1, y1), (x2, y2))
        line_endpoints.append(endpoints)

    fin.close()
    return line_endpoints

def solve(inputfile, should_register_diag_line):
    line_endpoints = parse_input(inputfile)
    vent = HydroVent(line_endpoints, should_register_diag_line)
    return vent.count_overlapped_points()

