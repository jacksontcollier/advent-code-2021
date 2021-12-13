#!/usr/bin/env python3

import day12
import cave_map

edge_list = day12.parse_input('test1_input.txt')
cm = cave_map.CaveMap(edge_list)
cm.compute_end_paths()
print("Part One (Test 1): %d" % cm.get_num_end_paths())
edge_list = day12.parse_input('test2_input.txt')
cm = cave_map.CaveMap(edge_list)
cm.compute_end_paths()
print("Part One (Test 2): %d" % cm.get_num_end_paths())
edge_list = day12.parse_input('test3_input.txt')
cm = cave_map.CaveMap(edge_list)
cm.compute_end_paths()
print("Part One (Test 2): %d" % cm.get_num_end_paths())
edge_list = day12.parse_input('input_day12.txt')
cm = cave_map.CaveMap(edge_list)
cm.compute_end_paths()
print("Part One (Real): %d" % cm.get_num_end_paths())

