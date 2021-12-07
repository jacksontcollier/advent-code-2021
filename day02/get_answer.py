#!/usr/bin/env python3

from day02 import *

commands = input_file_to_list('input_day02.txt')
first_answer = calc_displacement_part_one(commands)
second_answer = calc_displacement_part_two(commands)
print("First answer: %d" % first_answer)
print ("Second answer: %d" % second_answer)
