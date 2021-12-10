#!/usr/bin/env python3

from day10 import *

test_lines = parse_input('test_input.txt')
syntax_score = get_illegal_char_syntax_score(test_lines)
print("Part One (Test Input): %d" % syntax_score)
input_lines = parse_input('input_day10.txt')
syntax_score = get_illegal_char_syntax_score(input_lines)
print("Part One: %d" % syntax_score)
median_autocomplete_score = get_median_autocomplete_score(test_lines)
print("Part Two (Test Input): %d" % median_autocomplete_score)
median_autocomplete_score = get_median_autocomplete_score(input_lines)
print("Part Two: %d" % median_autocomplete_score)
