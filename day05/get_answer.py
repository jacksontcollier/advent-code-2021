#!/usr/bin/env python3

from day05 import *

inputfile = 'input_day05.txt'
part_one_answer = solve(inputfile, should_register_diag_line = False)
part_two_answer = solve(inputfile, should_register_diag_line = True)
print('First part answer: %d' % part_one_answer)
print('Part two answer: %d' % part_two_answer)

