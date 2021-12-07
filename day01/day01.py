#!/usr/bin/env python3

from typing import List

def count_depth_increases(depths: List[int]) -> int:
    num_increases = 0

    if len(depths) < 2:
        return num_increases

    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            num_increases += 1

    return num_increases

def three_measurement_sliding_window(depths: List[int]) -> int:
    num_increases = 0

    if len(depths) < 4:
        return num_increases

    for i in range(3, len(depths)):
        prev_sum = depths[i-1] + depths[i-2] + depths[i-3]
        current_sum = depths[i] + depths[i-1] + depths[i-2]
        if current_sum > prev_sum:
            num_increases += 1

    return num_increases

def read_input_file_to_list(input_file: str) -> List[int]:
    depths = []
    fin = open(input_file)

    for line in fin.readlines():
        depths.append(int(line.rstrip()))

    return depths

