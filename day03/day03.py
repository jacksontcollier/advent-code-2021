#!/usr/bin/env python3

import copy
from typing import List

def get_life_support_rating(diagnostics: List[str]) -> int:
    oxygen_generator_rating = calc_bit_criteria_rating(diagnostics, 'oxygen')
    co2_scrubber_rating = calc_bit_criteria_rating(diagnostics, 'CO2')
    return oxygen_generator_rating * co2_scrubber_rating

def calc_bit_criteria_rating(diagnostics: List[str], bit_criteria: str) -> int:
    diagnostics = copy.deepcopy(diagnostics)
    num_bits = len(diagnostics[0])

    for bit_pos in range(0, num_bits):
        if len(diagnostics) == 1:
            break
        bit_pos_count = [0, 0]

        for code in diagnostics:
            bit_pos_count[int(code[bit_pos])] += 1

        target_bit = ''

        if bit_criteria == 'oxygen':
            if bit_pos_count[1] >= bit_pos_count[0]:
                target_bit = '1'
            else:
                target_bit = '0'
        elif bit_criteria == 'CO2':
            if bit_pos_count[0] <= bit_pos_count[1]:
                target_bit = '0'
            else:
                target_bit = '1'

        diagnostics[:] = [code for code in diagnostics if code[bit_pos] ==
                target_bit]


    print("Length of diagnostics -- %s: %d" % (bit_criteria, len(diagnostics)))
    return int(diagnostics[0], 2)

def calc_power_consumption(diagnostics: List[str]) -> int:
    bit_pos_count = [{ "0": 0, "1": 0 } for char in diagnostics[0]]

    for code in diagnostics:
        for i in range(0, len(code)):
            bit_pos_count[i][code[i]] += 1

    gamma_rate = ''
    epsilon_rate = ''

    for bit_count in bit_pos_count:
        if bit_count['0'] > bit_count['1']:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate * epsilon_rate

def infile_to_list(infile: str) -> List[str]:
    fin = open(infile)
    diagnostics = []

    for line in fin.readlines():
        diagnostics.append(line.rstrip())

    fin.close()
    return diagnostics
