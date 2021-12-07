#!/usr/bin/env python3

from typing import List

def calc_displacement_part_two(commands: List[str]) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        command, magnitude = command.split()
        magnitude = int(magnitude)

        if command == 'forward':
            horizontal_position += magnitude
            depth += aim * magnitude
        elif command == 'down':
            aim += magnitude
        elif command == 'up':
            aim = max(0, aim - magnitude)

    return depth * horizontal_position

def calc_displacement_part_one(commands: List[str]) -> int:
    horizontal_position = 0
    depth = 0

    for command in commands:
        command, magnitude = command.split()
        magnitude = int(magnitude)

        if command == 'forward':
            horizontal_position += magnitude
        elif command == 'down':
            depth += magnitude
        elif command == 'up':
            depth = max(0, depth - magnitude)

    return depth * horizontal_position

def input_file_to_list(inputfile: str) -> List[str]:
    fin = open(inputfile)
    commands = []

    for line in fin.readlines():
        commands.append(line.rstrip())

    fin.close()
    return commands

