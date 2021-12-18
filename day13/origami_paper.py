#!/usr/bin/env python3

import copy

class OrigamiPaper(object):
    def __init__(self, positions, fold_positions):
        self.max_col = positions[0][0]
        self.max_row = positions[0][1]
        self.original_state = []
        self.state = []
        self.fold_positions = fold_positions
        self.fold_index = 0

        for pos in positions:
            col, row = pos
            self.max_col = max(self.max_col, col)
            self.max_row = max(self.max_row, row)

        for i in range(0, self.max_row + 1):
            self.original_state.append(['.' for j in range(0, self.max_col + 1)])

        for pos in positions:
            col, row = pos
            self.original_state[row][col] = '#'

        self.state = copy.deepcopy(self.original_state)

    def print_original_state(self):
        for row in self.original_state:
            for val in row:
                print(val, end='')
            print()

    def has_next_fold(self):
        return self.fold_index < len(self.fold_positions)

    def fold(self):
        fold_direction, fold_position = self.fold_positions[self.fold_index]

        if fold_direction == 'x':
            self.vertical_fold(fold_position)
        else:
            self.horizontal_fold(fold_position)

        self.fold_index += 1

    def horizontal_fold(self, fold_position):
        self.state = self.state[0:fold_position]
        bottom_part = self.state[fold_position:]
        bottom_part = list(reverse(bottom_part))

