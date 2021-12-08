#!/usr/bin/env python3

from bingo_board import BingoBoard

def parse_inputfile(inputfile):
    fin = open(inputfile)
    bingo_boards = []

    values = [int(value) for value in ((fin.readline()).rstrip()).split(',')]
    fin.readline()

    board_rows = []
    row_counter = 0
    while (line := fin.readline()):
        if line == '\n':
            continue
        board_row = [int(val) for val in (line.rstrip()).split()]
        board_rows.append(board_row)
        row_counter += 1
        if row_counter == 5:
            bingo_boards.append(BingoBoard(board_rows))
            row_counter = 0
            board_rows = []

    return (values, bingo_boards)

def solve_part_one(inputfile):
    values, bingo_boards = parse_inputfile(inputfile)

    for val in values:
        for board in bingo_boards:
            if board.has_val(val):
                board.mark_val(val)
                if board.get_has_won():
                    return board.calc_final_score()

