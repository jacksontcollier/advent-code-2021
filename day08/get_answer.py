#!/usr/bin/env python3

from day08 import *

test_input_entries = parse_input('test_input.txt')
num_unique_segments = count_unique_segment_digits(test_input_entries)
print("Part One (Test Input): %d" % num_unique_segments)
input_entries = parse_input('input_day08.txt')
num_unique_segments = count_unique_segment_digits(input_entries)
print("Part One: %d" % num_unique_segments)
test_sum = sum_output_values(test_input_entries)
print("Part Two (Test Input): %d" % test_sum)
input_sum = sum_output_values(input_entries)
print("Part Two: %d" % input_sum)

