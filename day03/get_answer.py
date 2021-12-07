#!/usr/bin/env python3

from day03 import *

diagnostics = infile_to_list('input_day03.txt')
first_answer = calc_power_consumption(diagnostics)
second_answer = get_life_support_rating(diagnostics)
print('First answer: %d' % first_answer)
print('Second answer: %d' % second_answer)

