#!/usr/bin/env python3

from signal_pattern import SignalPattern

digit_to_segment_count = {
    0: 6, 1: 2, 2: 5, 3: 5, 4: 4,
    5: 5, 6: 6, 7: 3, 8: 7, 9: 6
}

def parse_input(inputfile):
    fin = open(inputfile)
    entries = []

    for line in fin:
        left_half, right_half = line.strip().split('|')
        signal_patterns = [pattern for pattern in left_half.split()]
        output_values = [val for val in right_half.split()]
        entry = (signal_patterns, output_values)
        entries.append(entry)

    fin.close()
    return entries

def count_unique_segment_digits(entries):
    unique_segment_digit_counts = [
        digit_to_segment_count[1],
        digit_to_segment_count[4],
        digit_to_segment_count[7],
        digit_to_segment_count[8]
    ]
    num_unique_segment_digits = 0

    for entry in entries:
        signal_patterns, output_values = entry
        for value in output_values:
            if len(value) in unique_segment_digit_counts:
                num_unique_segment_digits += 1

    return num_unique_segment_digits

def decode_signal_mapping(signal_pattern_strings):
    signal_patterns = []
    for pattern in signal_pattern_strings:
        signal_patterns.append(SignalPattern(pattern))

    one = None
    four = None
    seven = None
    eight = None

    for i, signal_pattern in enumerate(signal_patterns):
        if signal_pattern.get_segment_count() == 2:
            one = signal_pattern
        if signal_pattern.get_segment_count() == 4:
            four = signal_pattern
        if signal_pattern.get_segment_count() == 3:
            seven = signal_pattern
        if signal_pattern.get_segment_count() == 7:
            eight = signal_pattern

    signal_patterns.remove(one)
    signal_patterns.remove(four)
    signal_patterns.remove(seven)
    signal_patterns.remove(eight)

    six = None
    six_index = 0

    for i, signal_pattern in enumerate(signal_patterns):
        if signal_pattern.get_segment_count() == 6 and \
           signal_pattern.num_segments_common(one) == 1:
            six = signal_pattern
            six_index = i

    del signal_patterns[six_index]

    nine = None
    nine_index = 0

    for i, signal_pattern in enumerate(signal_patterns):
        if signal_pattern.get_segment_count() == 6 and \
           signal_pattern.num_segments_common(four) == four.get_segment_count():
            nine = signal_pattern
            nine_index = i

    del signal_patterns[nine_index]

    zero = None
    zero_index = 0

    for i, signal_pattern in enumerate(signal_patterns):
        if signal_pattern.get_segment_count() == 6 and \
           signal_pattern.num_segments_common(seven) == seven.get_segment_count() \
           and signal_pattern.num_segments_common(four) == 3:
            zero = signal_pattern
            zero_index = i

    del signal_patterns[zero_index]

    three = None
    three_index = 0

    for i, signal_pattern in enumerate(signal_patterns):
        if signal_pattern.get_segment_count() == 5 \
           and signal_pattern.num_segments_common(one) == \
               one.get_segment_count():
            three = signal_pattern
            three_index = i

    del signal_patterns[three_index]

    five = None
    five_index = 0

    for i, signal_pattern in enumerate(signal_patterns):
        if signal_pattern.get_segment_count() == 5 \
           and signal_pattern.num_segments_common(four) == 3:
            five = signal_pattern
            five_index = i

    del signal_patterns[five_index]

    two = signal_patterns[0]

    signal_pattern_mapping = {
        zero.get_segment_str(): 0,
        one.get_segment_str(): 1,
        two.get_segment_str(): 2,
        three.get_segment_str(): 3,
        four.get_segment_str(): 4,
        five.get_segment_str(): 5,
        six.get_segment_str(): 6,
        seven.get_segment_str(): 7,
        eight.get_segment_str(): 8,
        nine.get_segment_str(): 9
    }

    return signal_pattern_mapping

def sum_output_values(entries):
    sum = 0
    for entry in entries:
        signal_pattern_strs, output_values = entry
        decode_mapping = decode_signal_mapping(signal_pattern_strs)
        sum_str = ''
        for value in output_values:
            sum_str += str(decode_mapping[''.join(sorted(value))])
        sum += int(sum_str)

    return sum

