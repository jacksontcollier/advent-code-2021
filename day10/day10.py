#!/usr/bin/env python3

opening_chars = set(['(', '[', '{', '<'])
closing_chars = set([')', ']', '}', '>'])
opening_to_closing_chars = { '(': ')', '[': ']', '{': '}', '<': '>' }
char_to_syntax_score = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
autocomplete_score_map = { ')': 1, ']': 2, '}': 3, '>': 4 }

def parse_input(inputfile):
    fin = open(inputfile)
    lines = []

    for line in fin.readlines():
        lines.append(line.strip())

    fin.close()
    return lines

def find_illegal_char(line):
    unclosed_chars = []
    most_recent_open_char = None
    for char in line:
        if char in opening_chars:
            unclosed_chars.append(char)
            most_recent_open_char = unclosed_chars[len(unclosed_chars)-1]
        elif (char in closing_chars) and (not most_recent_open_char):
            return char
        elif (char in closing_chars) \
              and (opening_to_closing_chars[most_recent_open_char] != char):
            return char
        elif (char in closing_chars) \
              and (opening_to_closing_chars[most_recent_open_char] == char):
            unclosed_chars.pop()
            if len(unclosed_chars) > 0:
                most_recent_open_char = unclosed_chars[len(unclosed_chars)-1]
            else:
                most_recent_open_char = None

    return None

def get_closing_chars(incomplete_line):
    unclosed_chars = []
    most_recent_open_char = None
    sequence_closing_chars = ''

    for char in incomplete_line:
        if char in opening_chars:
            unclosed_chars.append(char)
        elif char in closing_chars:
            unclosed_chars.pop()

    for char in reversed(unclosed_chars):
        sequence_closing_chars += opening_to_closing_chars[char]

    return sequence_closing_chars


def find_illegal_chars(lines):
    illegal_chars = []

    for line in lines:
        illegal_char = find_illegal_char(line)
        if illegal_char:
            illegal_chars.append(illegal_char)

    return illegal_chars

def get_illegal_char_syntax_score(lines):
    illegal_chars = find_illegal_chars(lines)
    syntax_scores = [char_to_syntax_score[char] for char in illegal_chars]
    return sum(syntax_scores)

def discard_corrupt_lines(lines):
    incomplete_lines = []

    for line in lines:
        illegal_char = find_illegal_char(line)
        if not illegal_char:
            incomplete_lines.append(line)

    return incomplete_lines

def get_autocomplete_score(line):
    closing_chars = get_closing_chars(line)
    score = 0

    for char in closing_chars:
        score *= 5
        score += autocomplete_score_map[char]

    return score

def get_median_autocomplete_score(lines):
    autocomplete_scores = []
    lines = discard_corrupt_lines(lines)

    for line in lines:
        autocomplete_scores.append(get_autocomplete_score(line))

    autocomplete_scores.sort()
    return autocomplete_scores[int(len(autocomplete_scores) / 2)]

