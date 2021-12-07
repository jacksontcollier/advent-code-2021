#!/usr/bin/env python3

from day01 import *

depths = read_input_file_to_list('input_day01.txt')
first_part_answer = count_depth_increases(depths)
second_part_answer = three_measurement_sliding_window(depths)
print('First part answer:', first_part_answer)
print('Second part answer:', second_part_answer)
